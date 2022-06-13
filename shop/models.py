from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    CATEGORY=(
        ('rent','rent'),
        ('sale','sale'),
    )

    name = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY) 
    place = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    owner = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(tag)


    def __str__(self):
        return self.name



class orders(models.Model):
    STATUS=(
        ('booked','booked'),
        ('sold','sold'),
    )

    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)


   

    