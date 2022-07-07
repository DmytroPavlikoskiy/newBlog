from django.shortcuts import render, redirect, get_object_or_404
from sqlalchemy import and_

from .models import News, LikeNews
from .forms import NewsForm, UserRegisterForm, UserLogin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView, CreateView, FormView


def home(request):
    news = News.objects.order_by('-date')
    return render(request, 'main/home.html', {'news': news})


def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'main/news_home.html', {'news': news})


def one_news(request, id):
    user_id = request.user.id
    news = News.objects.get(id=id)
    likes = LikeNews.objects.filter(news_id=news.id, user_id=user_id)
    print(likes)
    return render(request, 'main/one_news.html', {'news': news, 'likes': likes})


def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Данні були введені не коректно!!!'
    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_news.html', data)


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print('do')
        if form.is_valid():
            print('pis9')
            form.save()
            messages.success(request,'Ви успішно зареєстрованні!')
            return redirect('login')
        else:
            print(form)
    else:
        form = UserRegisterForm()
    return render(request, 'main/register_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        print('do')
        if form.is_valid():
            print('pis9')
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLogin()
    return render(request, 'main/login_user.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')


def add_like(request, news_id):
    user_id = request.user.id
    likes = LikeNews.objects.filter(news_id=news_id, user_id=user_id)
    if likes:
        likes.delete()
    else:
        like = LikeNews()
        like.news_id = news_id
        like.user_id = request.user.id
        like.save()
        print(likes)

    return redirect('/one_news/' + str(news_id))



