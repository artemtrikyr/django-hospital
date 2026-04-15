from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'patient_name', 'birth_date', 'phone', 'complaints', 
            'appointment_date', 'doctor', 'diagnosis', 'treatment'
        ]
        
        # Створюємо спільний набір стилів для всіх полів
        base_attrs = {
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all duration-200 shadow-sm bg-white'
        }

        widgets = {
            'patient_name': forms.TextInput(attrs=base_attrs),
            'phone': forms.TextInput(attrs=base_attrs),
            'diagnosis': forms.TextInput(attrs=base_attrs),
            'doctor': forms.Select(attrs=base_attrs),
            
            # Спеціальні типи полів з тими ж стилями
            'birth_date': forms.DateInput(attrs={**base_attrs, 'type': 'date'}),
            'appointment_date': forms.DateTimeInput(attrs={**base_attrs, 'type': 'datetime-local'}),
            
            # Текстові області (complaints, treatment)
            'complaints': forms.Textarea(attrs={**base_attrs, 'rows': 3}),
            'treatment': forms.Textarea(attrs={**base_attrs, 'rows': 3}),
        }