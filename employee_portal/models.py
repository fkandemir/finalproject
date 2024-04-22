from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.IntegerField()
    kilometres = models.IntegerField()
    color = models.CharField(max_length=50)
    engine_capacity = models.FloatField()
    fuel_type = models.CharField(max_length=50)
    doors = models.IntegerField()
    gearbox_type = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.model_year}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    #profile_picture = models.ImageField

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Client(models.Model):

    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
    ]

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #profile_picture = models.ImageField

    def __str__(self):
        return f"{self.name} {self.surname}"

    

    