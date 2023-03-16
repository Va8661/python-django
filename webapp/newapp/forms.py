from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'age', 'email', 'phone', 'date', 'time', 'symptoms']
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'email': 'Email',
            'phone': 'Phone Number',
            'date': 'Appointment Date',
            'time': 'Appointment Time',
            'symptoms': 'Symptoms',
        }
