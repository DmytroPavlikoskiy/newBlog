from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('news', news_home, name='news'),
    path('one_news/<int:id>/', one_news, name='one_news'),
    path('create', create_news, name='create'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_user, name='register'),
    path('like/<int:news_id>', add_like, name='like')
]