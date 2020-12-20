from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect,Http404
from django.views import View
#download file
import os
from django.conf import settings
from django.db.models import Q
from shop.models import Product, ProductImages,User,Payment
from instamojo_wrapper import Instamojo
from digitalShop.settings import PAYMENT_API_KEY, PAYMENT_AUTH_TOKEN
api = Instamojo(api_key=PAYMENT_API_KEY, auth_token=PAYMENT_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')
import math
def createPayment(request, product_id):
    product=Product.objects.get(id=product_id)
    amount=(product.price-(product.price *(product.discount/100)))
    user=request.session.get('user')
    userObj=User.objects.get(id=user.get('id'))
    # Create a new Payment Request
    response = api.payment_request_create(
            amount=math.floor(amount),
            purpose=f'Payment for {product.name}',
            send_email=True,
            email=user.get('email'),
            phone=userObj.phone,
            buyer_name=userObj.name,
            redirect_url="http://localhost:8000/complete-payment"
    )
    url= response['payment_request']['longurl']
    payment_request_id= response['payment_request']['id']
    #print(response)
    payment=Payment(product=product,user=User(id=user.get('id') ),payment_request_id=payment_request_id )
    payment.save()
    return redirect(url)


def paymentSuccess(request):
    payment_id=request.GET.get('payment_id')
    payment_status=request.GET.get('payment_status')
    payment_request_id=request.GET.get('payment_request_id')
    # Create a new Payment Request
    response = api.payment_request_payment_status(payment_request_id, payment_id)
    status=response['payment_request']['payment']['status']
    if status !='Failed':
        payment=Payment.objects.get(payment_request_id=payment_request_id)
        payment.payment_id =response['payment_request']['payment']['payment_id']
        payment.status=status
        payment.save()
        return render(request, 'shop/payment_success.html', {'title': 'Payment Success','payment':payment})
    else:
        print('failed')
        return render(request, 'shop/payment_failed.html', {'title': 'Payment Failed'})

def downloadProduct(request, product_id):
    try:
        product=Product.objects.get(id=product_id)
        session_user=request.session.get('user')
        user=User(id=session_user.get('id'))
        payment=Payment.objects.filter(product=product, user=user)
        if len(payment)>0:
            # fill these variables with real values
            return HttpResponse('download')
        else:
            return redirect('home')
    except:
        return HttpResponse('error')

def my_orders(request):
    user_id=request.session.get('user').get('id')
    user=User(id=user_id)
    payments=Payment.objects.filter(~Q(status ='Failed'),user=user)
    return render(request, 'shop/my_orders.html',{'orders':payments})
    
