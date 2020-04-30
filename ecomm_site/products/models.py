import django
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Product(models.Model):
    """
    A single Product
    """
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name







