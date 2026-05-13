from django.db import models

class Product(models.Model):
    name=models.CharField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.CharField()
    image=models.ImageField(upload_to='products/')