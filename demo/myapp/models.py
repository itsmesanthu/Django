from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    stantend=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    image=models.ImageField()
    def __str__(self):
        return self.name

