from django.db import models
from OnlineCartApp.models import Products
from django.db.models import F, Sum

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)


class Orders(models.Model):
    product = models.ManyToManyField(Products)
    totalprice = models.IntegerField()

    def get_total_price(self):
        return self.Products.price * self.OrderItem.quantity

