from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import WebUserCreationForm, UserLogin
from .models import WebUser
import pdb


def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'registration/create.html')

#@login_required(login_url='/example url you want redirect/') #redirect when user is not logged in
@login_required
def home(request):
    pdb.set_trace()
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        pdb.set_trace()
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], pasword=form.cleaned_data['password'])
            login(request, user)
            return redirect('home')
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = WebUserCreationForm(request.POST)
        #
        if form.is_valid():
            WebUser.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user = authenticate(username=form.cleaned_data['username'], pasword=form.cleaned_data['password']) # para cuando el usuario ya esta creado
            return redirect('login')
    return render(request, 'index.html')

