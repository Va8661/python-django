import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
from django.utils.datastructures import MultiValueDictKeyError
from django.db import transaction

def hi(request):
    return render(request,'newapp/home.html')

@transaction.atomic
def book_appointment(request):
    if request.method == 'POST':
        name = request.POST['firstName'] + ' ' + request.POST['lastName']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        symptoms = request.POST['symptoms']
        # Generate a random token number
        token_number = random.randint(1, 100)
        appointment = Appointment(
            name=name,
            age=age,
            email=email,
            phone=phone,
            date=date,
            time=time,
            symptoms=symptoms,
            token_number=token_number
        )
        appointment.save()
        return render(request, 'newapp/book_appointment.html', {'token_number': token_number})
    else:
        return render(request, 'newapp/book_appointment.html')

