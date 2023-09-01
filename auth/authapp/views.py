from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm,UserCreationForm

def home(request):
    return render ( request , 'authapp/base.html' )

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'authapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Replace with your desired redirection

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'authapp/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect after logout
