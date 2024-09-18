# views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json


def index(request):
    return render(request, 'products/index.html')


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            price = data.get('price')

            if not name or not price or float(price) <= 0:
                return JsonResponse({'error': 'Invalid data'}, status=400)

            product = Product.objects.create(name=name, description=description, price=price)
            return JsonResponse({'id': product.id, 'name': product.name, 'description': product.description, 'price': str(product.price)}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def get_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)
