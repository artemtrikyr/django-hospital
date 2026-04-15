from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'appointment_date', 'doctor')
    list_filter = ('appointment_date', 'doctor')