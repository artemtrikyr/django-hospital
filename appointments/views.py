from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Appointment
from .forms import AppointmentForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AppointmentSerializer


@api_view(['GET'])
def api_appointment_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

def is_doctor(user):
    return user.groups.filter(name='Doctors').exists() or user.is_superuser

def is_admin(user):
    return user.groups.filter(name='Admins').exists() or user.is_superuser

def appointment_list(request):
    appointments = Appointment.objects.all()
    diagnosis_filter = request.GET.get('diagnosis')
    
    if diagnosis_filter:
        appointments = appointments.filter(diagnosis__icontains=diagnosis_filter)
    
    return render(request, 'appointments/list.html', {
        'appointments': appointments,
        'current_filter': diagnosis_filter
    })

def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    request.session['last_viewed_id'] = appointment.id
    request.session['last_viewed_name'] = appointment.patient_name
    
    return render(request, 'appointments/detail.html', {'appointment': appointment})

def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Новий запис'})

@user_passes_test(is_doctor)
def appointment_edit(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail', id=appointment.id)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Редагування запису'})

@user_passes_test(is_doctor)
def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'delete_confirm.html', {'obj': appointment, 'back_url': 'appointment_list'})