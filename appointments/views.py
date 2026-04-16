from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm

# 1. СПИСОК
def appointment_list(request):
    appointments = Appointment.objects.all()
    diagnosis_filter = request.GET.get('diagnosis')
    
    if diagnosis_filter:
        appointments = appointments.filter(diagnosis__icontains=diagnosis_filter)
    
    return render(request, 'appointments/list.html', {
        'appointments': appointments,
        'current_filter': diagnosis_filter
    })

# 2. ДЕТАЛІ
def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'appointments/detail.html', {'appointment': appointment})

# 3. СТВОРЕННЯ
@login_required
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Новий запис'})

# 4. РЕДАГУВАННЯ
@login_required
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

# 5. Видалення 
@login_required
def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'delete_confirm.html', {'obj': appointment, 'back_url': 'appointment_list'})