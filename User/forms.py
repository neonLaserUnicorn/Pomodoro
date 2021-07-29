from .models import Users
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')