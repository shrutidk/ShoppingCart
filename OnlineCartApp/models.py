from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    #owner = models.ForeignKey('auth.User',related_name='products', on_delete=models.CASCADE)


    class Meta:
        ordering=['price']

