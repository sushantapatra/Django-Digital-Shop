from django.db import models
from shop.models import Product,User


class Payment(models.Model):
    product=models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    user=models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    payment_request_id=models.CharField(max_length=250,null=False,unique=True)
    payment_id=models.EmailField(max_length=200, unique=False,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200,default='Failed')