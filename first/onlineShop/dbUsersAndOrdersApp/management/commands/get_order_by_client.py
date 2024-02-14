from django.core.management.base import BaseCommand
from dbUsersAndOrdersApp.models import Product, Client, Order
from random import choice


class Command(BaseCommand):
    help = "Get all products by Client."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        result = []
        if client is not None:
            order = Order.objects.filter(client=client).first()
            if order is not None:
                products = order.products.all()
                result = ", ".join(product.name for product in products)
                self.stdout.write(
                    f'Клиент {client.name} заказал {result} на сумму {order.total_price}')
            else:
                self.stdout.write(f'Клиент сделал заказ')
        else:
            self.stdout.write(f'Клиента не существует')
