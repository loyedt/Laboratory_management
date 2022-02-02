from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def book(request):
    if request.method == 'POST':
        name    = request.POST['name']
        email   = request.POST['email']
        phone   = request.POST['phone']
        time    = request.POST['time']
        date    = request.POST['date']
        message = request.POST['message']

        appointment = name + " " +phone + " " +time + " " +date + " " +message 

        #send an email
        send_mail(
            'Appointment Request', # subject
            appointment, # message
            email, # From mail
            ['loyedthomas1999@gmail.com'],# To mail
        )
        return render(request,'appoinment.html')
