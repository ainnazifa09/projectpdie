#models.py
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.TextField(max_length=128, primary_key=True)
    idd = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    numphone = models.CharField(max_length=15)
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=20)