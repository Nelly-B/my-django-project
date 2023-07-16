from django.db import models
from django.utils import timezone

# Create your models here.
class CommonField(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    home_phone_number = models.CharField(max_length=20, unique=True) 
    home_address = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Patient(CommonField):
    office_phone_number = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=30, null=True)
    marital_status = models.CharField(max_length=20, null=True) 
    age = models.CharField(max_length=30)
    nin = models.CharField(max_length=30, unique=True)
    office_address = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=30)
    photo = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'Patients'

    def __str__(self):
        return f'{self.age}, {self.nin}'
    
    def fullname(self):
        return f'{self.last_name}, {self.middle_name} {self.first_name}'

class Emergency(CommonField):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, unique=True)
    relationship = models.CharField(max_length=50)
    photo = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'Emergency contact information'

        def __str__(self):
            return f'{self.relationship}'

class Allergy(models.Model):
    patient = models.ManyToManyField(Patient)
    name = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'Allergies'