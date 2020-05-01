from django.shortcuts import render
from .models import Cart

from django.views.generic import DetailView


class CartDetailView(DetailView):
    queryset = Cart.objects.all()





