from django.shortcuts import render, redirect
from .models import Chores
from .forms import UserForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.


def cur_user(request):
    all_chores = Chores.objects.all
    return render(request, 'template.html', locals())


def new_user(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
    form = UserForm
    data = {
        'user': form
    }

    return render(request, 'add_user.html', data)


def login(request):
    return render(request, 'login.html')