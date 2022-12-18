from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import login

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'webapp/login/login.html', context=context)

def home_page(request):
    context = {
        login: "login"
    }
    return render(request, 'webapp/home_page/index.html', context=context)

