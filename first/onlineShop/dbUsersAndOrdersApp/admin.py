from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    # fields = ['name', 'email', 'phone_number', 'adress']
    readonly_fields = ['reg_date']
    fieldsets = [
        (
            'Основная информация',
            {
                'classes': ['wide'],
                'fields': ['name', 'email']
            }
        ),
        (
            'Информация для доставки',
            {
                'classes': ['collapse'],
                'fields': ['phone_number', 'adress']
            }
        ),
        (
            'Информация о регистрации',
            {
                'fields': ['reg_date']
            }
        ),
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['add_date',
                    'name',
                    'price',
                    'count']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по описанию'
    readonly_fields = ['add_date']
    fieldsets = [
        (
            'Основная информация',
            {
                'classes': ['wide'],
                'fields': ['name', 'price']
            }
        ),
        (
            'Дополнительная информация',
            {
                'classes': ['collapse'],
                'fields': ['description', 'image']
            }
        ),
        (
            'Информация о продукте',
            {
                'fields': ['count', 'add_date']
            }
        ),
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['total_price', 'date_ordered']
    fieldsets = [
        (
            'Клиент',
            {
                'fields': ['client']
            }
        ),
        (
            'Продукт',
            {
                'fields': ['products']
            }
        ),
        (
            'Сумма и дата заказа',
            {
                'fields': ['total_price', 'date_ordered']
            }
        ),
    ]
