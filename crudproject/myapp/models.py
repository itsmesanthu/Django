from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    place=models.CharField(max_length=100)
    job=models.CharField(max_length=30)
    salary=models.IntegerField()
    def __str__(self):
        return self.name