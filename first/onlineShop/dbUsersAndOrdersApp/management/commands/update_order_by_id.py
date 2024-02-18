from django.core.management.base import BaseCommand
from dbUsersAndOrdersApp.models import Product, Order
from random import choice

class Command(BaseCommand):
    help = "Update order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')      
    
    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            for _ in range(3):
                rand_product = choice(products)
                order.products.add(rand_product)
                order.total_price += rand_product.price
            self.stdout.write(f'Заказ {pk} обновлён')
            order.save()
        else:
            self.stdout.write(f'Заказ не существует')
        