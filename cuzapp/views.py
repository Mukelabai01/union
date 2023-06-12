from contextlib import _RedirectStream
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User,GroupManager
from .models import Appointment
from django.core.mail import send_mail




# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def success_view(request):
    return render(request, 'services.html')       




def create_appointment(request):
    if request.method == 'POST':
        faculty = request.POST.get('faculty')
        course = request.POST.get('course')
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        Phone = request.POST.get('Phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        new_appointment = Appointment(
            faculty=faculty,
            course=course,
            date=date,
            time=time,
            name=name,
            Phone=Phone,
            email=email,
            message=message
        )
        new_appointment.save()

        # Send email notification to the admin
        #subject = 'New Appointment Submission'
        #message = f'A new appointment has been submitted. Please log in to the database to see the information.'
        #admin_email = 'mukelabai.maboshe@techtitan.co.zm'  # Replace with the admin's email address
        #send_mail(subject, message, 'noreply@example.com', [admin_email])


        return redirect('success_view')  # Redirect to a success page after saving the appointment
    else:
        return render(request, 'index.html')



