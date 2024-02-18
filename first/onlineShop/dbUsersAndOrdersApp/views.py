from datetime import datetime, date, time, timedelta
from django.http import HttpResponse
from django.shortcuts import render
from .models import Order, Client
import pandas as pd

# Create your views here.

def index(request):
    return render(request, "dbUsersAndOrdersApp/index.html")

def client(request):
    if request.method == "POST":
        pk = request.POST.get("client_id")
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            context = {
                "client" : client.name,
                "pk" : pk
            }
            return render(request, "dbUsersAndOrdersApp/client.html", context)
        else:
            return HttpResponse("Такого пользователя нет в базе данных")

def by_period(request, pk, days):
    client = Client.objects.filter(pk=pk).first()
    seven_days_ago = datetime.now() - timedelta(days=days)
    orders = Order.objects.filter(client=client, date_ordered__gte = seven_days_ago)
    orders_dict = {}
    for order in orders:
        products = []
        for product in order.products.all():
            products.append(str(product))
        orders_dict[order.date_ordered] = products
    context = {
          'period' : days,
          'client' : client.name,
          'count': len(orders),
          'orders' : orders_dict
        }
    return render(request, "dbUsersAndOrdersApp/filter.html", context)