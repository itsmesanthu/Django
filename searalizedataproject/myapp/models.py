from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.TextField()
    brand=models.CharField(max_length=20)
    def __str__(self):
        return self.name