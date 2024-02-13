from django.db import models

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.TextField()
    user_type = models.CharField(max_length=30)
