from django.contrib import admin
from .models import Patient, Emergency


# Register your models here.
admin.site.register(Patient)
admin.site.register(Emergency)
