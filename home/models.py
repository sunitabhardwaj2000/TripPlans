from django.db import models

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=100)
    travel_date = models.DateField()
    persons = models.IntegerField()

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
]

status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='Pending'
)

def __str__(self):
        return self.name