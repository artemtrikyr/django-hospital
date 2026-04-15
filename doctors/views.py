from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor
from .forms import DoctorForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {'doctors': doctors})

@login_required
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list') # переконайся, що такий name є в urls.py
    else:
        form = DoctorForm()
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Додати лікаря'})

@login_required
def doctor_edit(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Редагувати лікаря'})


@login_required
def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'delete_confirm.html', {'obj': doctor, 'back_url': 'doctor_list'})