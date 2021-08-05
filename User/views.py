from django.shortcuts import render, redirect
from .models import Chores
from .forms import UserForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.


def cur_user(request):
    all_chores = Chores.objects.filter(author=request.user.username)
    return render(request, 'user.html', locals())


def new_user(request):
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
            auth_user = authenticate(username=user.username, password=user.password)
            login(request, user)
            return redirect('current user')
    form = RegisterForm
    data = {
        'user': form
    }

    return render(request, 'add_user.html', data)


class LogInView(LoginView):
    template_name = 'login.html'
    form_class = UserForm
    success_url = reverse_lazy('current user')

    def get_success_url(self):
        return self.success_url

def new_task(request):
    task = Chores(author=request.user.username)
    task.save()
    return redirect('current user')

def clear_tasks(request):
    all_chores = Chores.objects.filter(author=request.user.username)
    for item in all_chores:
        Chores.delete(item)
    return redirect('current user')

def ret_tasks(request):
    all_chores = Chores.objects.filter(author=request.user.username)
    data = [{'id':item.id, 'name':item.name, 'author':item.author, 'complete':item.complete, 'create_time':item.create_time} for item in all_chores]

    return render(request, 'tasks.html', locals())