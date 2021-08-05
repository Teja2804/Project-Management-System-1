from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

# from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']