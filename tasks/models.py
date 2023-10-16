from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()



class Tasks(models.Model):
    title = models.CharField(max_length=199)
    description = models.TextField(max_length=400)
    due_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)