from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    place=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name