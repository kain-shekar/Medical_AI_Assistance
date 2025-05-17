from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'phone','medical_history')
    search_fields = ('name', 'email', 'phone')

