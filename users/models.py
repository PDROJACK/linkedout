from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    isEmployer = models.BooleanField()