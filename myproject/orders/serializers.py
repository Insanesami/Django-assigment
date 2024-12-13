from rest_framework import serializers
from .models import Product, Order, Customer, Seller

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def validate_name(self,value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product with name Already exists.")
        return value
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


