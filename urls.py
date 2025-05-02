from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('quiz/', views.quiz_start, name='quiz_start'),
    path('quiz/run/', views.quiz_run, name='quiz_run'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
path('register/', views.register, name='register'),
path('login/', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),
path('profile/', views.profile, name='profile'),
path('about/', views.about, name='about'),
path('literature/', views.literature, name='literature'),  # 🔹 литература
path('videos/', views.videos, name='videos'),              # 🔹 видео
path('articles/', views.articles, name='articles'),

]
