from django.db import models
from django.contrib.auth.models import User
class Leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    leave_type=models.CharField(max_length=20)
    start_date=models.DateField()
    End_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
