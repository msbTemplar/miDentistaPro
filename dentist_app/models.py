from django.db import models

# Create your models here.



class Dentist(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=2000)
    service_price = models.DecimalField('Service Price', max_digits=10, decimal_places=2)
   
    
    def __str__(self):
        return f"{self.service_name} {self.service_price}"

class ServiceImage(models.Model):
    #service_image_name = models.CharField(max_length=100, verbose_name="Nombre del Servicio")
    service_image_name = models.ForeignKey(Service, blank=True, null=True, on_delete=models.CASCADE)
    service_image_description = models.TextField(verbose_name="Descripción")
    service_image_image = models.ImageField(upload_to='services/', verbose_name="Imagen")
    
    def __str__(self):
        return self.service_image_namename
    
class DentistImage(models.Model):
    dentist_image_name = models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
    dentist_image_description = models.TextField(verbose_name="Descripción")
    dentist_image_image = models.ImageField(upload_to='dentists/', verbose_name="Imagen")
    
    def __str__(self):
        return self.dentist_image_name
    
class Appointment(models.Model):
    #appointment_service = models.CharField('Select Service', max_length=100)
    appointment_service=models.ForeignKey(Service, blank=True, null=True, on_delete=models.CASCADE)
    #appointment_doctor = models.CharField('Select Doctor', max_length=100)
    appointment_doctor=models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
    appointment_name = models.CharField('Name', max_length=200)
    appointment_email = models.EmailField('Email')
    appointment_phone = models.CharField('Phone', max_length=15)
    appointment_address = models.CharField('Address', max_length=500)
    appointment_city = models.CharField('City', max_length=200)
    appointment_country = models.CharField('Country', max_length=200)
    appointment_date = models.DateField('Appointment Date')
    appointment_time = models.TimeField('Appointment Time')
    appointment_message = models.CharField('Message', max_length=2000)
    appointment_status = models.BooleanField('Set/Not?', default=False)
    
    def __str__(self):
        return f"{self.appointment_name} - {self.appointment_email}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Message from {self.name} - {self.subject}'
    

class Newsletter(models.Model):
    email = models.EmailField(unique=True)  # Almacenará el correo electrónico
    date_subscribed = models.DateTimeField(auto_now_add=True)  # Fecha de suscripción
    is_active = models.BooleanField(default=True)  # Permitir activar o desactivar la suscripción

    def __str__(self):
        return self.email