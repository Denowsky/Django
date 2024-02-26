from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            'add_date'
        ]
        labels = {'name': 'Имя',
                  'description': 'Описание',
                  'price': 'Цена',
                  'count': 'Количество'}
