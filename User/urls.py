from django.urls import path
from .views import cur_user, new_user, LogInView, new_task, clear_tasks, ret_tasks

urlpatterns = [
    path('', cur_user, name='current user'),
    path('add/', new_user, name='new user'),
    path('log/', LogInView.as_view(), name='login'),
    path('new_chore/', new_task, name='new task'),
    path('clear/', clear_tasks, name = 'clear'),
    path('task_data', ret_tasks, name = 'tasks_json')
]