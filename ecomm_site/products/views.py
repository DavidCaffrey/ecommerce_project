from django.shortcuts import render
from .models import Product
from django.views.generic import ListView


class ProductListView(ListView):
    model = Product
    # if pagination required
    # paginate_by = 100

