from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {
        'doctors': doctors
    })