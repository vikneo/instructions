from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class AuthFormUser(AuthenticationForm):
    """

    """
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label = "Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )


class RegisterFormUser(UserCreationForm):
    """

    """
    username = forms.CharField(
        label = 'Логин',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label = 'Повторить пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
