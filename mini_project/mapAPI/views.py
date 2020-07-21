from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# from shop.models import Product
# from .forms import AddProductForm
# from .cart import Cart


def map_test(request):
    
    return render(request, 'mapAPI/map_test.html')

def main_test(request):
   
    return render(request, 'mapAPI/main_v2.0.html')

