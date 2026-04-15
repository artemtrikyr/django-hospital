from django.shortcuts import render, get_object_or_404
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all()
    diagnosis_filter = request.GET.get('diagnosis')
    
    if diagnosis_filter:
        appointments = appointments.filter(diagnosis__icontains=diagnosis_filter)
    
    return render(request, 'appointments/list.html', {
        'appointments': appointments,
        'current_filter': diagnosis_filter
    })

# Додай цю функцію для перегляду повної інформації
def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'appointments/detail.html', {'appointment': appointment})