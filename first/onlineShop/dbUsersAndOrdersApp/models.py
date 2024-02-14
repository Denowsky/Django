from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adress = models.TextField()
    reg_date = models.DateField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places = 2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_ordered = models.DateField(auto_now_add=True)