from django.core.management.base import BaseCommand
from dbUsersAndOrdersApp.models import Product, Client, Order
from random import choice

class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')      
    
    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        print(client.name)
        if client is not None:
                order = Order(client = client)
                for _ in range(3):
                    rand_product = choice(products)
                    order.products.add(rand_product)
                    order.total_price += rand_product.price
                order.save()
                self.stdout.write(f'Заказ {order.date_ordered} создан')
        else:
            self.stdout.write(f'Клиента не существует')
        
