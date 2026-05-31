from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=20)
    dob=models.DateField()
    job=models.CharField(max_length=20)
    place=models.CharField(max_length=100)
    email=models.EmailField()
