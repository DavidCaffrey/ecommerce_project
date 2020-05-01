from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    # if pagination required
    # paginate_by = 100


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product does not exist Dave")
    #     return instance

    # def get_object(self):
        # obj = super().get_object()
        # Record the last accessed date
        # obj.save()
        # return obj
