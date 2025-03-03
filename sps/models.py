from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100,blank=True)
    razorpay_id = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)