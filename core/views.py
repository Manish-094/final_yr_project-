
from django.shortcuts import redirect, render
from django.views.generic import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request,'core/home.html')

def ContactUs(request):
    return render(request,'core/contactus.html')

def Covid19data(request):
    return render(request,'core/covid19data.html')
    

def AboutUs(request):
    return render(request,'core/aboutus.html')

def Chatbot(request):
    return render(request,'core/chatbot.html')
        

class SignupView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request,'core/signup.html',{'form':fm})
    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Successfully !")
            return redirect('/signup')
        else:
            return render(request,'core/signup.html',{'form':fm})
        
class MyLoginView(View):
    def get(self,request):
        fm = MyLoginForm()
        return render(request,'core/login.html',{'form':fm})
    
    def post(self,request):
        fm = MyLoginForm(request,data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"You Are Login Successfully !")
                return redirect('/')
            else:
                return render(request,'core/login.html',{'form':fm})
        else:
            return render(request,'core/login.html',{'form':fm})
        
        
