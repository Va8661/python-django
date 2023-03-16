import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return render(request,'newapp/home.html')
def book_appointment(request):
     
    if request.method == 'POST':
        # Generate a random token number
        token_number = random.randint(1, 100)
        return render(request, 'newapp/book_appointment.html', {'token_number': token_number})
    else:
        return render(request, 'newapp/book_appointment.html')