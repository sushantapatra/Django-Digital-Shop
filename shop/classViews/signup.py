from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.views import View
from shop.models import Product, ProductImages,User
from django.contrib.auth.hashers import make_password,check_password

class SignupView(View):
    def get(self, request):
        return render(request, 'shop/signup.html', {'title': 'Signup Form'})
    
    def post(self, request):
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
            return render(request, 'shop/signup.html', {'title': 'Signup Foignup Form','error':'Email or Password Invalid'})
        

