from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from shop.models import Product, ProductImages,User,Payment
from shop.utils.email_sender import sendEmail
# Create your views here.


def index(request):
    # sendEmail(name="Sushanta Patra", email='development.experiment@gmail.com',subject="Test Email",htmlContent="<h1>Email from Python by Sendinblue</h1>")
    products = Product.objects.filter(active=True)
    params = {
        'title': 'Home',
        'products': products
    }
    return render(request, 'shop/index.html', params)


def productDetails(request, product_id):
    products = Product.objects.get(id=product_id)
    images = ProductImages.objects.filter(product=product_id)
    download_url=None
    try:
        session_user=request.session.get('user')
        if session_user:
            user_id=session_user.get('id')
            user=User(id=user_id)
            payment=Payment.objects.filter(~Q(status='Failed'),product=products, user=user)
            if len(payment) !=0:
                if (products.file):
                    download_url=product.file.url
                else:
                    download_url=product.file.link

    except:
        pass
    return render(request, 'shop/product_details.html', {'title': 'Product Details', 'product': products, 'images': images,'download_url':download_url})


def signup(request):
    if request.method =='POST':
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            password=request.POST.get('password')
            confpassword=request.POST.get('repassword')
            if password == confpassword:
                hashpassword=make_password(password=password)
                user=User(name=name, email=email,phone=phone,password=hashpassword )
                user.save()
                return render(request, 'shop/login.html', {'title': 'Login Form'})
        except:
            return render(request, 'shop/signup.html', {'title': 'Signup Form','error':'Email already exists'})
    else:
        return render(request, 'shop/signup.html', {'title': 'Signup Form'})

def login(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
            flag=check_password(password=password, encoded=user.password)
            if flag:
                return redirect('home')
            else:
                return render(request, 'shop/login.html', {'title': 'Signup Form','error':'Email or Password Invalid'})
        except: 
            return render(request, 'shop/login.html', {'title': 'Signup Form','error':'Email or Password Invalid'})
        
    else:
        return render(request, 'shop/login.html', {'title': 'Signup Form'})


def downloadFree(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.discount==100:
            print('Hello')
            return HttpResponse('Download')
        else:
            return redirect('home')
    except:
        return redirect('home')

def sendOtp(request):
    return HttpResponse("{'message':'success'}")
