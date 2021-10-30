from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Signin 
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def lms(request):
    return render(request,'lms.html')

def docs(request):
     return render(request,'documentation.html')

def downloads(request):
     return render(request,'downloads.html')
  
    
def demo(request):
     return render(request,'demo.html')
   
    
def signin(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          password = request.POST.get('password')
          signin = Signin(name=name, email=email, password=password)
          signin.save()
          messages.success(request, 'your message has been sent')
     return render(request,'signin.html')
    
    
def about(request):
    return render("this is about page")
    