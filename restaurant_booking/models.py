# models.py
from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.IntegerField()

class Table(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# For user profile

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



