from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('orders/7/<int:pk>', views.by_period, name='orders', kwargs={'days':7}),
    path('orders/30/<int:pk>', views.by_period, name='orders', kwargs={'days':30}),
    path('orders/365/<int:pk>', views.by_period, name='orders', kwargs={'days':365}),
]

