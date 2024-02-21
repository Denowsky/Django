from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Order, Client, Product
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request, "dbUsersAndOrdersApp/index.html")


def by_period(request):
    pk = request.POST.get("client_id")
    client = Client.objects.filter(pk=pk).first()
    periods = [7, 30, 365]
    result = {}
    
    for period in periods:
        days = datetime.now() - timedelta(days=period)
        orders = Order.objects.filter(client=client, date_ordered__gte=days)
        
        orders_dict = {}
        for order in orders:
            products = [str(product) for product in order.products.all()]
            orders_dict[order.date_ordered] = products
        result[period] = orders_dict
    
    context = {
        'client': client.name,
        'orders': result
    }
    
    return render(request, "dbUsersAndOrdersApp/orders.html", context)

def product_form(request):
    if request.method == 'POST':
        try: 
            pk = request.POST.get("product_id")
            product = get_object_or_404(Product, pk=pk)
        except Exception:
            return HttpResponse("Такого товара нет в базе данных")
        form = ProductForm(instance=product)
        return render(request, 'dbUsersAndOrdersApp/product.html', {'form': form, 'product_id' : pk})
    
def save_product(request, pk):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        product = Product.objects.get(pk=pk)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.count = form.cleaned_data['count']
            product.image = form.cleaned_data['image']

            try:
                fs = FileSystemStorage()
                filename = fs.save(product.image.name, product.image)
                product.image = filename
                product.save()
                return HttpResponse("Продукт сохранён")
            except Exception as e:
                return HttpResponse("Произошла ошибка при сохранении продукта")