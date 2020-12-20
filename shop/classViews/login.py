from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.views import View
from shop.models import User
from django.contrib.auth.hashers import make_password,check_password

class LoginView(View):
    return_url=None
    def get(self, request):
        LoginView.return_url=request.GET.get('return_url')
        return render(request, 'shop/login.html', {'title': 'Signup Form'})
    
    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.get(email=email)
            flag=check_password(password=password, encoded=user.password)
            if flag:
                temp={}
                temp['id']=user.id
                temp['email']=user.email
                temp['name']=user.name
                temp['phone']=user.phone
                request.session['user']=temp
                #print(user.__dict__)
                if  LoginView.return_url:
                    return redirect( LoginView.return_url)
                return redirect('home')
            else:
                return render(request, 'shop/login.html', {'title': 'Signup Form','error':'Email or Password Invalid'})
        except: 
            return render(request, 'shop/login.html', {'title': 'Signup Form','error':'Email or Password Invalid'})
        

class LogoutView(View):
    def get(self, request):
        request.session.clear()
        return redirect('home')

class ResetPassword(View):
    def get(self, request):
        return render(request, 'shop/reset_password.html')


    def post(self, request):
        email=request.POST.get('email')
        print(email)
        return render(request, 'shop/reset_password.html')