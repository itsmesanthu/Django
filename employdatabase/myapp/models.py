from django.db import models

# Create your models here.
class employdata(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=6)
    dob=models.DateField()
    place=models.CharField(max_length=100)
    email=models.EmailField()

