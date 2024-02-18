from django.core.management.base import BaseCommand
from dbUsersAndOrdersApp.models import Client
from random import randint
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(
                name = ''.join(lorem_ipsum.words(1,common=False)).capitalize(),
                email = f'{"".join(lorem_ipsum.words(1,common=False))}@mail.com',
                phone_number = randint(79000000000, 79999999999),
                adress = ''.join(lorem_ipsum.paragraphs(1, common=False)).capitalize(),
                )
            client.save()
            self.stdout.write(f'{client.name}')