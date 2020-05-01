from django.db import models
from django.core.validators import MinValueValidator


class Cart(models.Model):
    cart_id = models.IntegerField(validators=[MinValueValidator(0)])
    customer_id = models.IntegerField(validators=[MinValueValidator(0)])
    employee_id = models.IntegerField(validators=[MinValueValidator(0)])
    order_date = models.DateTimeField(auto_now=True,)




