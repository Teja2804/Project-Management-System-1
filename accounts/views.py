from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import CreateUserForm
from .forms import LoginForm

##############baseindexpage######################################
def home(request):
    return render(request,"base.html", {'title':'index'})

######################register here###############################


def signupview(request):
    #if request.user.is_authenticated:
     #   return redirect('dashboard')
    #else:
        #form=CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                email=form.cleaned_data.get('email')
                messages.success(request, 'Account created successfully')
                return redirect('accounts:home')
                #return HttpResponse("User created successfully")
        else:
            form = CreateUserForm()
        return render(request,'register/signup.html',{'form':form , 'title':'register here'})
        #return redirect('home')


def loginpage(request):
   # form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)
        #username=request.POST('username')
        #password=request.POST('password')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect('home')
            #return HttpResponse("User incorrect") 
            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f' welcome {username} !!')
                return redirect("{% url('board:dashboard') %}")
            else:
                messages.info(request,'Username or Password is incorrect')  
        else:
            messages.info(request,'Username or Password is incorrect')
    form = LoginForm()
    return render(request,'register/login.html',context={"login_form":form})


#@login_required(login_url="login/")
def dashboardView(request):
    return HttpResponse("This is dashboard")


def logoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')
# when entered to admin shows messages, 
# unable to redirect to dashboard

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "register/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail('subject', 'email', 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="register/password_reset.html", context={"password_reset_form":password_reset_form})