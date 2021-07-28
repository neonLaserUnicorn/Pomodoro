from django.shortcuts import render, redirect
from .models import Chores, Users
from .forms import UserForm

# Create your views here.

this_user = UserForm()


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
    error = ''
    if request.method == 'POST':
        #auth = False
        user = UserForm(request.POST)
        if user.is_valid():
            user1=Users(user)
            all_users = Users.objects.all()
            for i in all_users:
                if user1.user_name == i.user_name:
                    if user1.user_password == i.user_password:
                        return redirect('new user')

        error = 'Bad input'

    form = UserForm
    data = {
        'user': form,
        'error': error
    }
    return render(request, 'login.html', data)
