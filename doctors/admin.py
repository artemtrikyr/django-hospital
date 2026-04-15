from django.contrib import admin # type: ignore
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'experience')
    search_fields = ('full_name',)