from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    # if pagination required
    # paginate_by = 100


class ProductDetailView(DetailView):
    queryset = Product.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.save()
        return obj
