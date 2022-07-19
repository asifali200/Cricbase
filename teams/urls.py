from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home, name="home"),
    path('gallery', views.gallery, name="gallery"),  
    path('test', views.test, name="test"), 
    path('newsheading', views.newsheading,name='newsheading'),
    path('news/<news_id>', views.news,name='news'),
    path('team', views.team,name='team'),
    path('player/<player_id>', views.player,name='player'),
    path('about',views.about,name="about"), 
    path('search', views.search, name='search'),  
    path('quiz',views.quiz,name="quiz"),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('feedback', auth_view.LoginView.as_view(template_name='feedback.html'), name="feedback"),
]