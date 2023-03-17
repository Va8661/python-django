from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['firstname', 'lastname', 'age', 'email', 'phone', 'date', 'time', 'symptoms']
        labels = {
            'firstname': 'Full Name',
            'lastname': 'Full Name',
            'age': 'Age',
            'email': 'Email',
            'phone': 'Phone Number',
            'date': 'Appointment Date',
            'time': 'Appointment Time',
            'symptoms': 'Symptoms',
        }
