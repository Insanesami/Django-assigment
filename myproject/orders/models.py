from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    
class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.models.CharField(max_length=15)
    
class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    
    
class platfromApiCall(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_url = models.URLField()
    requested_data= models.JSONField()
    response_data = models.JSONField()
    
