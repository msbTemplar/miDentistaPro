from django.contrib import admin
from .models import Dentist,Service,Appointment,ContactMessage,Newsletter

# Register your models here.

admin.site.register(Dentist)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(ContactMessage)
admin.site.register(Newsletter)