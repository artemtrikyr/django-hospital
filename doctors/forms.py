from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'experience']
        
        base_attrs = {
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none shadow-sm'
        }

        widgets = {
            'full_name': forms.TextInput(attrs=base_attrs),
            'specialization': forms.TextInput(attrs=base_attrs),
            'experience': forms.NumberInput(attrs=base_attrs),
        }