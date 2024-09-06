from django.shortcuts import render
from .models import Product

def show_main(request):
    # Get the first product
    # product = Product.objects.first()

    # Prepare context
    # context = {
    #     'name': product.name,
    #     'price': product.price,
    #     'description': product.description,
    # }

    # Prepare pre-made context
    context = {
        'name': 'Birkenstock Boston',
        'price': 2599000,
        'description': 'Birkenstock Boston adalah sandal yang nyaman digunakan untuk berbagai aktivitas.'
    }

    return render(request, 'main.html', context)