from django.db import models
from django.utils import timezone
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now())


    def buy_product(self):
        pass




