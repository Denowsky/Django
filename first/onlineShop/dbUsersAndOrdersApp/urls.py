from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.by_period, name='orders'),
    path('product/', views.product_form, name='orders'),
    path('product/save/<int:pk>', views.save_product, name='orders'),
]

