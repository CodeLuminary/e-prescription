from django.db import models

# Create your models here.
class Drug(models.Model):
    name = models.TextField()
    description = models.TextField()


