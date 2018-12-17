# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html', {'products': Product.objects.all()})

def goToProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'prod': product})
