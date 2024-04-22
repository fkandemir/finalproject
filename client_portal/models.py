from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Client(models.Model):

    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    #gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_picture = models.ImageField(upload_to='client_photos/', blank=True, null=True)  # Store images in the 'client_photos/' directory

    def __str__(self):
        return f"{self.name} {self.surname}"

    

    
