from django import forms
from .models import Dentist,Appointment,Service,ContactMessage,Newsletter,ServiceImage,DentistImage

class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = ['nombre', 'apellido', 'especialidad', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Name',
                'style': 'height: 55px;'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Surname',
                'style': 'height: 55px;'
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Specialty',
                'style': 'height: 55px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Phone',
                'style': 'height: 55px;'
            }),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_service', 'appointment_doctor', 'appointment_name', 'appointment_email', 'appointment_phone', 'appointment_address', 'appointment_city','appointment_country','appointment_date','appointment_time','appointment_message','appointment_status']
        labels = {
            'appointment_service': 'Select Service',
            'appointment_doctor': 'Select Doctor',  # Cambia la etiqueta aquí
        }
        widgets = {
            'appointment_service': forms.Select(attrs={
                'class': 'form-select border-0 bg-light px-4',
                'placeholder': 'Select Service',
                'style': 'height: 55px;'
            }),
            'appointment_doctor': forms.Select(attrs={
                'class': 'form-select border-0 bg-light px-4',
                'placeholder': 'Select Doctor',
                'style': 'height: 55px;'
            }),
            'appointment_name': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Name',
                'style': 'height: 55px;'
            }),
            'appointment_email': forms.EmailInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
            'appointment_phone': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Phone',
                'style': 'height: 55px;'
            }),
            'appointment_address': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Address',
                'style': 'height: 55px;'
            }),
            'appointment_city': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your City',
                'style': 'height: 55px;'
            }),
            'appointment_country': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Country',
                'style': 'height: 55px;'
            }),
            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Appointment Date',
                'style': 'height: 55px;',
                'type': 'date'  # Selector de fecha (día, mes, año)
            }),
            'appointment_time': forms.TimeInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Appointment Time',
                'style': 'height: 55px;',
                'type': 'time',  # Selector de hora (hora, minutos)
                'step': '1'
            }),
            'appointment_message': forms.Textarea(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Appointment Message',
                'style': 'height: 55px;'
            }),
            'appointment_status': forms.CheckboxInput(attrs={
                'class': 'form-check-input border-0 bg-dark px-4',
                'placeholder': 'Appointment Status',
                'style': 'height: 35px;'
            }),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'service_description', 'service_price']
        labels = {
            'service_name': 'Service Name',
            'service_description': 'Service Description',  # Cambia la etiqueta aquí
        }
        widgets = {
            'service_name': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Service Name',
                'style': 'height: 55px;'
            }),
            'service_description': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Service Description',
                'style': 'height: 55px;'
            }),
            'service_price': forms.NumberInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Service Price',
                'style': 'height: 55px;'
            }),
            
        }

class ServiceImageForm(forms.ModelForm):
    class Meta:
        model = ServiceImage
        fields = ['service_image_name', 'service_image_description', 'service_image_image']
        widgets = {
            'service_image_name': forms.Select (attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': 'Ingrese el nombre del servicio' , 'style': 'height: 55px;'}),
            'service_image_description': forms.Textarea(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': 'Ingrese la descripción' , 'style': 'height: 55px;'}),
            'service_image_image': forms.ClearableFileInput(attrs={'class': 'form-control border-0 bg-light px-4' , 'style': 'height: 55px;'}),
        }

class DentistImageForm(forms.ModelForm):
    class Meta:
        model = DentistImage
        fields = ['dentist_image_name', 'dentist_image_description', 'dentist_image_image']
        widgets = {
            'dentist_image_name': forms.Select (attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': 'Seleccione el nombre del dentista' , 'style': 'height: 55px;'}),
            'dentist_image_description': forms.Textarea(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': 'Ingrese la descripción' , 'style': 'height: 55px;'}),
            'dentist_image_image': forms.ClearableFileInput(attrs={'class': 'form-control border-0 bg-light px-4' , 'style': 'height: 55px;'}),
        }
        
        
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Name',
                'style': 'height: 55px;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Email',
                'style': 'height: 55px;',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Subject',
                'style': 'height: 55px;',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-0 bg-light px-4',
                'placeholder': 'Your Message',
                'style': 'height: 200px;',
            }),
        }
        

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']  # Solo necesitamos el correo electrónico
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-white p-3',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
        }
        labels = {
            'email': ''
        }