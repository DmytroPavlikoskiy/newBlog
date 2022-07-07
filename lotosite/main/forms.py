from .models import News
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput,\
Textarea, CharField, EmailField, EmailInput,ImageField, FileField
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'date', 'full_text', 'image_post']

        widgets = {
            'title': TextInput(attrs={
                'class': 'inp1',
                'placeholder': 'Назва'
            }),
            'anons': TextInput(attrs={
                'class': 'inp2',
                'placeholder': 'Анонс'
            }),
            'date': DateTimeInput(attrs={
                'class': 'inp2',
                'placeholder': 'Дата публікації'
            }),
            'full_text': Textarea(attrs={
                'class': 'inp2',
                'placeholder': 'Новина'
            }),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': TextInput(attrs={
                'class': 'inp1',
                'placeholder': "Ваше ім'я"
            }),
            'email': EmailInput(attrs={
                'class': 'inp2',
                'placeholder': 'Електронна Пошта'
            }),
            'password1': TextInput(attrs={
                'class': 'inp3',
                'placeholder': 'Пароль'
            }),
            'password2': TextInput(attrs={
                'class': 'inp4',
                'placeholder': 'Повторіть пароль'
            })
        }


class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'inp1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'inp3'}))