from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse

from django.contrib import messages

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .forms import LoginForm


def home(request):
    return render(request,"base.html")

@login_required(login_url="login/")
def dashboardView(request):
    return HttpResponse("This is dashboard")

def signupview(request):
    #if request.user.is_authenticated:
     #   return redirect('dashboard')
    #else:
        form=CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account created successfully')
                #return redirect('login')
                #return HttpResponse("User created successfully")
        else:
            form = CreateUserForm()
            return render(request,'register/signup.html',{'form':form})
        return redirect('home')


def loginpage(request):
   # form=LoginForm()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Username or Password is incorrect')  
       # if form.is_valid():
            #form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect('home')
            #return HttpResponse("User incorrect")
    #else:
     #   form = LoginForm()
    context={}
    return render(request,'register/login.html',context)

def logoutView(request):
    logout(request)
    return redirect('login')
# when entered to admin shows messages, 
# unable to redirect to dashboard
