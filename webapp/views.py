from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import login

from .models import folder, file


def loginUser(request):
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

def worker(request):
    context = {
        'folder': folder.objects.filter(department=request.user.department_user)
    }
    return render(request, 'webapp/working_page/index.html', context=context)

def show_folder(request, folder_id):
    flget = folder.objects.get(pk=folder_id)
    context = {
        'folder': folder.objects.get(pk=folder_id),
        'file': file.objects.filter(parent_directory=flget),
        'folder_id': folder_id
    }
    return render(request, 'webapp/folder_page/index.html', context=context)