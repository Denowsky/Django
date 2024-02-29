from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adress = models.TextField()
    reg_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places = 2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now=True)
    image = models.ImageField(default='default.jpg')

    def __str__(self) -> str:
        return f'Товар: {self.name}, цена: {self.price}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Заказ от {self.date_ordered}'
    
    def save(self, *args, **kwargs) -> None:
        super(Order, self).save(*args, **kwargs)
        total_price = sum(product.price for product in self.products.all())
        self.total_price = total_price
        super(Order, self).save(*args, **kwargs)