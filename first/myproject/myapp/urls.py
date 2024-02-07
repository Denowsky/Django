from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Главная'),
    path('about/', views.about, name='Обо мне'),
]