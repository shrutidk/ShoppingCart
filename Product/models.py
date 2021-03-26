from django.db import models
from OnlineCartApp.models import Products
from django.contrib.auth import get_user_model
#from django.db.models import F, Sum
import computed_property
#from rest_framework.response import Response,status
# Create your models here.


class Orders(models.Model):
    #product = models.CharField(max_length=100)
    product = models.ManyToManyField(Products)
    User = get_user_model()
    cust = models.ForeignKey(User, related_name='prodorders', on_delete=models.CASCADE)
    #cust = models.ForeignKey('Users.User',related_name='prodorders',on_delete=models.CASCADE)
    totalprice= computed_property.ComputedIntegerField(compute_from='calcprice')
    orderquantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['orderquantity']

    def calcprice(self):
        if Products.objects.get(name=self.product).quantity >= self.orderquantity:
            v=Products.objects.get(name=self.product)
            v.quantity=v.quantity - self.orderquantity
            v.save()
            return self.orderquantity*Products.objects.get(name=self.product).price
        else:
            return 0