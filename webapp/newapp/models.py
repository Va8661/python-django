from django.db import models

# Create your models here.
class Appointment(models.Model):
    firstName = models.CharField(max_length=30, default='')
    lastName = models.CharField(max_length=30, default='')
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.TextField(default='')
    name = models.CharField(max_length=200, default='')
    token_number = models.IntegerField()

    def __str__(self):
        return self.firstName + " " + self.lastName