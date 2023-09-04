from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from .models import CustomUser
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.    shortcuts import render, redirect
from .forms import CustomAuthenticationForm,UserCreationForm

def home(request):
    return render ( request , 'authapp/base.html' )

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Create a new user if the form is valid and username is unique
                user = form.save()
                # Log the user in (optional)
                login(request, user)
                # Redirect to a success page or login page
                return redirect('home')
            except IntegrityError:
                # Handle the case where the username is not unique
                form.add_error('username', 'This username is already taken.')
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'authapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email , password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                
                form.add_error(None, 'Invalid email or password.')    

    else:
        form = CustomAuthenticationForm()

    return render(request, 'authapp/login.html',{'form': form} )

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect after logout
