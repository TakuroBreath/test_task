from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/products/', views.get_products, name='get_products'),
    path('api/products/create/', views.create_product, name='create_product'),
]
