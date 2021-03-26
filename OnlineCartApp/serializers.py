from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Products
        fields = ['id','name','price','quantity']

    # def validate(self,data):
    #     if data['quantity'] < 0:
    #         raise serializers.ValidationError("Quantity cannot be negative")
    #     if data['quantity'] is None:
    #         raise serializers.ValidationError("Quantity cannot be blank")
    #     if data['price'] < 0:
    #         raise serializers.ValidationError("Price cannot be negative")


    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.title = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)

        instance.save()
        return instance

