from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('faculty','name', 'email', 'course','time','date','Phone','message')  # Customize the displayed fields

admin.site.register(Appointment, AppointmentAdmin)
# Register your models here.

# Register your models here.
