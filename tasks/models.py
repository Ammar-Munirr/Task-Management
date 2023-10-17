from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()



TASK_STATUS = (
    ('TO-DO', 'TO-DO'),
    ('IN-PROGRESS', 'IN-PROGRESS'),
    ('DONE', 'DONE'),
)

class Tasks(models.Model):
    title = models.CharField(max_length=199)
    description = models.TextField(max_length=400)
    due_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=13,choices=TASK_STATUS,default='TO-DO')