from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from .forms import LoginForm
from history.models import History




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request,user)
                history = History(username=username, user=user)
                history.save()
                return redirect('profile')
            else:
                 messages.danger(request, f'error')
    return render(request, 'users/login.html', {'form': form})
                 
                 

def logout(request, methods=['GET', "POST"]):
    auth.logout(request)
    return redirect('login')
   
             

@login_required
def profile(request):
    return render(request, 'users/profile.html')