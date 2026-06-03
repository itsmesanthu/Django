from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=100)
    marks=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name
