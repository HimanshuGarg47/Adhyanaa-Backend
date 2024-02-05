from django.db import models

# Create your models here.
from django.db import models

class CareerProfessional(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name