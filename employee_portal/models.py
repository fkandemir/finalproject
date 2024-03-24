from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.model_year}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} {self.surname}"