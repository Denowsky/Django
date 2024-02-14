from django.core.management.base import BaseCommand
from dbUsersAndOrdersApp.models import Product
from random import randint, uniform
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create product."
    
    def handle(self, *args, **kwargs):

        for i in range(10):
            product = Product(
                name = ''.join(lorem_ipsum.words(1,common=False)).capitalize(),
                description = ''.join(lorem_ipsum.paragraphs(1, common=False)).capitalize(),
                price = round(uniform(10.00, 999.00),2),
                count = randint(1,10)
                )
            product.save()
            self.stdout.write(f'{product.name}')