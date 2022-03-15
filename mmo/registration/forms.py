from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from allauth.account.forms import LoginForm

from .models import Profile


# Создаём форму LoginForm для входа в кабинет
class LoginForm(LoginForm):
    class Meta:
        model = User
        fields = ('username', 'password')


# регистрация пользователя, переопределяю форму allauth
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'first_name', 'last_name', 'email')