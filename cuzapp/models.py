from django.db import models

# Create your models here.

class Appointment(models.Model):
    faculty = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
