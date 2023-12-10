# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import WebUser

class WebUserCreationForm(forms.Form):  
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())