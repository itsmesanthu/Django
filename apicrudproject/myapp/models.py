from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    place=models.CharField(max_length=100)
    def __str__(self):
        return self.name