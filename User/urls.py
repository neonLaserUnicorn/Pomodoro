from django.urls import path
from .views import cur_user, new_user, LogInView

urlpatterns = [
    path('', cur_user, name='current user'),
    path('add/', new_user, name='new user'),
    path('log/', LogInView.as_view(), name='login')
]