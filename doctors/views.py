from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Doctor
from .forms import DoctorForm
import urllib.parse

def is_admin(user):
    return user.groups.filter(name='Admins').exists() or user.is_superuser

def doctor_list(request):
    spec_query = request.GET.get('spec')
    
    if spec_query is not None:
        spec_filter = spec_query.strip()
    else:
        raw_cookie = request.COOKIES.get('last_spec', '')
        spec_filter = urllib.parse.unquote(raw_cookie)

    doctors = Doctor.objects.all()
    if spec_filter:
        doctors = doctors.filter(specialization__icontains=spec_filter)

    response = render(request, 'doctors/list.html', {
        'doctors': doctors,
        'current_spec': spec_filter
    })

    if spec_query is not None:
        if spec_query.strip() == "":
            response.delete_cookie('last_spec')
        else:
            encoded_spec = urllib.parse.quote(spec_filter)
            response.set_cookie('last_spec', encoded_spec, max_age=86400)

    return response

@user_passes_test(is_admin)
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Додати лікаря'})

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'delete_confirm.html', {'obj': doctor, 'back_url': 'doctor_list'})