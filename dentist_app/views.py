from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from datetime import datetime
from django.contrib.auth import logout
from .forms import DentistForm,AppointmentForm,ServiceForm,ContactMessageForm,NewsletterForm,ServiceImageForm,DentistImageForm
from .models import Appointment,Dentist,Service,ContactMessage,ServiceImage,DentistImage
from django.contrib import messages
from django.http import JsonResponse


def all_the_options_view(request):
    #la_lista_des_services_images = ServiceImage.objects.all()  # Recupera todos los servicios
    return render(request, 'dentist_app/all_the_options_view.html', {})

def set_cookie_consent(request):
    response = JsonResponse({'status': 'ok'})
    response.set_cookie('cookie_consent', 'true', max_age=365*24*60*60)  # 1 año
    return response


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            # Guarda el email en la base de datos
            subscription = form.save(commit=False)
            email = subscription.email
            form.save()
            # Envía un correo de confirmación
            send_mail(
                'Subscription Confirmed',
                'Thank you for subscribing to our newsletter! with your email: ' + email,
                email,  # Email del remitente
                ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'],
            )

            # Muestra un mensaje de éxito
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')  # Redirige para evitar el reenvío de formularios

        else:
            # Mensaje de error si el formulario no es válido
            messages.error(request, 'Please provide a valid email.')

    else:
        form = NewsletterForm()  # Cargar un formulario vacío en caso de GET

    return render(request, 'dentist_app/home.html', {'form': form})


def service_form_view(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dentist_admin')  # Redirige a la página de inicio o a otra página después de guardar
    else:
        form = ServiceForm()
    return render(request, 'dentist_app/service_form.html', {'form': form})

def pricing_form_view(request):
    la_lista_des_appointments = Appointment.objects.all()
    context = {'la_lista_des_appointments': la_lista_des_appointments}
    return render(request, 'dentist_app/pricing_form.html',context )

def create_service_image_view(request):
    if request.method == 'POST':
        form = ServiceImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dentist_admin')  # Cambia esta URL por la vista que lista los servicios
    else:
        form = ServiceImageForm()
    
    return render(request, 'dentist_app/create_service_image.html', {'form': form})

def list_services_image_view(request):
    la_lista_des_services_images = ServiceImage.objects.all()  # Recupera todos los servicios
    return render(request, 'dentist_app/list_services_image_view.html', {'la_lista_des_services_images': la_lista_des_services_images})

def actualizar_services_image(request, id_service_image):
    services_image = ServiceImage.objects.get(pk=id_service_image)
    form = ServiceImageForm(request.POST or None, request.FILES or None,  instance=services_image)
    if form.is_valid():
        form.save()
        return redirect('list_services_image_view')
    context = {'services_image': services_image, 'form': form}
    return render(request, 'dentist_app/actualizar_services_image.html', context)

def eliminar_services_image(request, id_service_image):
    services_image = get_object_or_404(ServiceImage, id=id_service_image)
    services_image.delete()
    messages.success(request, "El Services Image ha sido eliminado con éxito.")
    return redirect('list_services_image_view')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal

def create_dentist_image_view(request):
    if request.method == 'POST':
        form = DentistImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dentist_admin')  # Cambia esta URL por la vista que lista los servicios
    else:
        form = DentistImageForm()
    
    return render(request, 'dentist_app/create_dentist_image.html', {'form': form})

def list_dentists_image_view(request):
    la_lista_des_dentists_images = DentistImage.objects.all()  # Recupera todos los servicios
    return render(request, 'dentist_app/list_dentists_image_view.html', {'la_lista_des_dentists_images': la_lista_des_dentists_images})

def actualizar_dentists_image(request, id_dentist_image):
    dentists_image = DentistImage.objects.get(pk=id_dentist_image)
    form = DentistImageForm(request.POST or None, request.FILES or None,  instance=dentists_image)
    if form.is_valid():
        form.save()
        return redirect('list_dentists_image_view')
    context = {'dentists_image': dentists_image, 'form': form}
    return render(request, 'dentist_app/actualizar_dentists_image.html', context)

def eliminar_dentists_image(request, id_dentist_image):
    dentists_image = get_object_or_404(DentistImage, id=id_dentist_image)
    dentists_image.delete()
    messages.success(request, "El Dentists Image ha sido eliminado con éxito.")
    return redirect('list_dentists_image_view')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal


def service_list_view(request):
    la_lista_des_servicios = Service.objects.all()
    context = {'la_lista_des_servicios': la_lista_des_servicios}
    return render(request, 'dentist_app/service_list_view.html',context )

def actualizar_service(request, id_service):
    service = Service.objects.get(pk=id_service)
    form = ServiceForm(request.POST or None, request.FILES or None,  instance=service)
    if form.is_valid():
        form.save()
        return redirect('service_list_view')
    context = {'service': service, 'form': form}
    return render(request, 'dentist_app/actualizar_service.html', context)


def eliminar_service(request, id_service):
    service = get_object_or_404(Service, id=id_service)
    service.delete()
    messages.success(request, "El Service ha sido eliminado con éxito.")
    return redirect('service_list_view')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal

def dentist_list_view(request):
    la_lista_des_dentistas = Dentist.objects.all()
    context = {'la_lista_des_dentistas': la_lista_des_dentistas}
    return render(request, 'dentist_app/dentist_list_view.html',context )

def actualizar_dentist(request, id_dentist):
    dentist = Dentist.objects.get(pk=id_dentist)
    form = DentistForm(request.POST or None, request.FILES or None,  instance=dentist)
    if form.is_valid():
        form.save()
        return redirect('dentist_list_view')
    context = {'dentist': dentist, 'form': form}
    return render(request, 'dentist_app/actualizar_dentist.html', context)

def eliminar_dentist(request, id_dentist):
    dentist = get_object_or_404(Dentist, id=id_dentist)
    dentist.delete()
    messages.success(request, "El Dentist ha sido eliminado con éxito.")
    return redirect('dentist_list_view')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'dentist_app/service_detail.html', {'service': service})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Dentist, id=doctor_id)
    return render(request, 'dentist_app/doctor_detail.html', {'doctor': doctor})

def actualizar_appointment(request, id_appointment):
    appointment = Appointment.objects.get(pk=id_appointment)
    form = AppointmentForm(request.POST or None, request.FILES or None,  instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('pricing_form')
    context = {'appointment': appointment, 'form': form}
    return render(request, 'dentist_app/actualizar_appointment.html', context)


def eliminar_appointment(request, id_appointment):
    appointment = get_object_or_404(Appointment, id=id_appointment)
    appointment.delete()
    messages.success(request, "El Appointment ha sido eliminado con éxito.")
    return redirect('pricing_form')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal

def appointment_form_view(request):
    if request.method == "POST":
        print(request.POST) 
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            appointment = form.save(commit=False)
            appointment.appointment_time = form.cleaned_data['appointment_time']
            appointment.save()
            return redirect('dentist_admin')  # Redirige a la página de inicio o a otra página después de guardar
    else:
        form = AppointmentForm()
        
    context = {'form': form}
    return render(request, 'dentist_app/appointment_form.html',context )

def dentist_admin_view(request):
    context = {'form': ''}
    return render(request, 'dentist_app/dentist_admin.html',context )

def dentist_form_view(request):
    if request.method == "POST":
        form = DentistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dentist_admin')  # Redirige a la página de inicio o a otra página después de guardar
    else:
        form = DentistForm()
    return render(request, 'dentist_app/dentist_form.html', {'form': form})
# Create your views here.
#def login(request):
    #return render(request, 'dentist_app/login.html',{})

def custom_logout_view(request):
    logout(request)
    return redirect('home') 


def home(request):
    services = Service.objects.all()
    doctors = Dentist.objects.all()
    context = {'services':services, 'doctors':doctors}
    return render(request, 'dentist_app/home.html',context)

def contact2(request):
    
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message_message = request.POST['message-message']
        
        #send email 
        send_mail(
            'Make appointment message from ' + message_name, # subject
            message_message, # message
            message_email, # from email
            ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'], # to email
        )
        
        return render(request, 'dentist_app/contact.html',{'message_name':message_name})
    else:
        return render(request, 'dentist_app/contact.html',{})
    
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            # Guardar el registro en la base de datos
            form.save()

            # Obtener los datos del formulario
            message_name = form.cleaned_data['name']
            message_email = form.cleaned_data['email']
            message_subject = form.cleaned_data['subject']
            message_message = form.cleaned_data['message']
            
            """
            # Enviar el correo electrónico
            send_mail(
                'Message from ' + message_name,  # Asunto
                message_message,  # Mensaje
                message_email,  # Correo electrónico del remitente
                ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'],  # Correos de destino
            )
            """
            email_content = f"""
            You have received a new contact message from {message_name}:

            Name: {message_name}
            Email: {message_email}
            Subject: {message_subject}
            Message: {message_message}
            """
            
            # Enviar el correo electrónico
            send_mail(
                f'Message from {message_name}',  # Asunto
                email_content,  # Cuerpo del correo con todos los detalles
                message_email,  # Correo electrónico del remitente
                ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'],  # Correos de destino
            )

            return render(request, 'dentist_app/contact.html', {'message_name': message_name})
    else:
        form = ContactMessageForm()

    return render(request, 'dentist_app/contact.html', {'form': form})

def contacts_list_view(request):
    # venue_list = Venue.objects.all().order_by('?')
    la_lista_de_contactos = ContactMessage.objects.all()
    name = request.user.username
   
    context = {'la_lista_de_contactos': la_lista_de_contactos, 'name':name}
    return render(request, 'dentist_app/contacts_list.html', context)


def actualizar_contacto(request, id_contacto):
    contacto = ContactMessage.objects.get(pk=id_contacto)
    form = ContactMessageForm(request.POST or None, request.FILES or None,  instance=contacto)
    if form.is_valid():
        form.save()
        return redirect('contacts_list')
    context = {'contacto': contacto, 'form': form}
    return render(request, 'dentist_app/actualizar_contacto.html', context)


def eliminar_contacto(request, id_contacto):
    contacto = get_object_or_404(ContactMessage, id=id_contacto)
    contacto.delete()
    messages.success(request, "El Contacto ha sido eliminado con éxito.")
    return redirect('contacts_list')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal



def about(request):
    return render(request, 'dentist_app/about.html',{})

def price(request):
    return render(request, 'dentist_app/price.html',{})

def service(request):
    return render(request, 'dentist_app/service.html',{})

def appointment(request):
    
    if request.method == 'POST':
        SERVICES_MAP = {
            "1": "Service 1",
            "2": "Service 2",
            "3": "Service 3",
        }
        DOCTORS_MAP = {
            "1": "Doctor 1",
            "2": "Doctor 2",
            "3": "Doctor 3",
        }
        # Obtener el identificador del servicio y doctor desde el formulario
        service_id = request.POST.get('services', None)
        service_name = SERVICES_MAP.get(service_id, "Servicio no encontrado")
        
        # Obtener la instancia del modelo Service basado en el ID recibido
        service_instance = Service.objects.get(id=service_id)  # Obtener la instancia del servicio
        
        doctor_id = request.POST.get('doctors', None)
        doctor_name = DOCTORS_MAP.get(doctor_id, "Doctor no encontrado")
        
        # Obtener la instancia del doctor, si es necesario
        doctor_instance = Dentist.objects.get(id=doctor_id)  # Si hay un modelo de Dentista
       
        
        services = request.POST.get('services', None)
        service_name = SERVICES_MAP.get(services, "Servicio no encontrado")
        doctors = request.POST.get('doctors', None)
        doctor_name = DOCTORS_MAP.get(doctors, "Doctor no encontrado")
        your_name = request.POST['your_name']
        your_email = request.POST['your_email']
        your_phone = request.POST['your_phone']
        your_address = request.POST['your_address']
        your_city = request.POST['your_city']
        your_country = request.POST['your_country']
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        your_mensaje = request.POST['your_mensaje']
        
        if appointment_date:
            # Convierte la fecha en un objeto datetime (opcional)
            fecha_seleccionada = datetime.strptime(appointment_date, '%m/%d/%Y')
            # Formatear la fecha como "20 noviembre 2024"
            fecha_formateada = fecha_seleccionada.strftime('%d %B %Y')
        appointment_time = request.POST['appointment_time']
        
        try:
            # Convierte la hora de AM/PM a 24 horas
            appointment_time_24hr = datetime.strptime(appointment_time, "%I:%M %p").strftime("%H:%M")
        except ValueError:
            # Si la conversión falla, maneja el error (puedes devolver un mensaje al usuario o dejarla vacía)
            appointment_time_24hr = None
        
        # Crear una nueva instancia del modelo Appointment
        appointment = Appointment(
            appointment_service=service_instance,  # Asignamos la instancia de Service
            appointment_doctor=doctor_instance,  # Asignamos la instancia de Dentist
            appointment_name=your_name,
            appointment_email=your_email,
            appointment_phone=your_phone,
            appointment_address=your_address,
            appointment_city=your_city,
            appointment_country=your_country,
            appointment_date=fecha_seleccionada,  # Guardamos la fecha como un objeto datetime
            #appointment_time=appointment_time,  # Guardamos la hora
            appointment_time=appointment_time_24hr,  # Guardamos la hora en formato de 24 horas
            appointment_message=your_mensaje,
            appointment_status=False  # O True, según tu lógica
        )
        
        # Guardar el objeto Appointment en la base de datos
        appointment.save()
        
        #send email 
        """
        send_mail(
            'Make appointment with this information: ' + your_name, # subject
            your_name + " \n" + your_email + " \n" + your_phone + " \n" + your_address + " \n" + your_city + " \n" + your_country + " \n" + service_name + " \n" + doctor_name + " \n" + appointment_date + " \n" + appointment_time + " \n" + your_mensaje, # message
            your_email, # from email
            ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'], # to email
        )
        """
        # Asunto del correo
        subject = 'Make appointment with this information: ' + your_name

        # Cuerpo del mensaje, añadiendo texto explicativo para cada campo
        message = (
            f"Name: {your_name} \n"
            f"Email: {your_email} \n"
            f"Phone: {your_phone} \n"
            f"Address: {your_address} \n"
            f"City: {your_city} \n"
            f"Country: {your_country} \n"
            f"Service: {service_name} \n"
            f"Doctor: {doctor_name} \n"
            f"Appointment Date: {appointment_date} \n"
            f"Appointment Time: {appointment_time} \n"
            f"Message: {your_mensaje}"
        )

        # Dirección de correo del remitente
        from_email = your_email

        # Lista de correos a los que se enviará el mensaje
        to_email = ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com']

        # Enviar el correo
        send_mail(
            subject,  # Asunto
            message,  # Cuerpo del mensaje
            from_email,  # Correo del remitente
            to_email  # Correos de destino
        )
        context={'your_name':your_name, 'service_name':service_name, 'doctor_name':doctor_name, 'appointment_date':appointment_date, 'appointment_time':appointment_time, 'your_mensaje':your_mensaje, 'your_email': your_email,'your_country':your_country, 'your_city':your_city , 'your_phone':your_phone, 'your_address':your_address}
        return render(request, 'dentist_app/appointment_other.html',context)
    else:
        # Obtener todos los servicios y doctores desde la base de datos
        """ services = Service.objects.all()
        doctors = Dentist.objects.all()
        print(Service.objects.all()) """
        return render(request, 'dentist_app/home.html',{})
    

def team(request):
    return render(request, 'dentist_app/team.html',{})

def testimonial(request):
    return render(request, 'dentist_app/testimonial.html',{})

def appointment_other(request):
    
    services = Service.objects.all()
    doctors = Dentist.objects.all()
    #context = {'services':services, 'doctors':doctors}
    
    if request.method == 'POST':
        """ SERVICES_MAP = {
            "1": "Service 1",
            "2": "Service 2",
            "3": "Service 3",
        }
        DOCTORS_MAP = {
            "1": "Doctor 1",
            "2": "Doctor 2",
            "3": "Doctor 3",
        } """
        
        """  services = Service.objects.all()
        doctors = Dentist.objects.all()
        #context = {'services':services, 'doctors':doctors}
        
        # Obtener el identificador del servicio y doctor desde el formulario
        service_id = request.POST.get('services', None)
        #service_name = SERVICES_MAP.get(service_id, "Servicio no encontrado")
        
        # Obtener la instancia del modelo Service basado en el ID recibido
        service_instance = Service.objects.get(id=service_id)  # Obtener la instancia del servicio
        
        doctor_id = request.POST.get('doctors', None)
        #doctor_name = DOCTORS_MAP.get(doctor_id, "Doctor no encontrado")
        
        # Obtener la instancia del doctor, si es necesario
        doctor_instance = Dentist.objects.get(id=doctor_id)  # Si hay un modelo de Dentista """
        
        """ services = request.POST.get('services', None)
        service_name = SERVICES_MAP.get(services, "Servicio no encontrado")
        doctors = request.POST.get('doctors', None)
        doctor_name = DOCTORS_MAP.get(doctors, "Doctor no encontrado") """
         # Obtener el ID del servicio y doctor desde el formulario
        service_id = request.POST.get('services', None)
        doctor_id = request.POST.get('doctors', None)

        # Obtener las instancias correspondientes de la base de datos
        service_instance = get_object_or_404(Service, id=service_id) if service_id else None
        doctor_instance = get_object_or_404(Dentist, id=doctor_id) if doctor_id else None
        
        your_name = request.POST['your_name']
        your_email = request.POST['your_email']
        your_phone = request.POST['your_phone']
        your_address = request.POST['your_address']
        your_city = request.POST['your_city']
        your_country = request.POST['your_country']
        #appointment_date = request.POST['appointment_date']
        appointment_date = request.POST.get('appointment_date')
        
        # Validación y formato de fecha
        if appointment_date:
            # Convierte la fecha en un objeto datetime (opcional)
            fecha_seleccionada = datetime.strptime(appointment_date, '%m/%d/%Y')
            # Formatear la fecha como "20 noviembre 2024"
            fecha_formateada = fecha_seleccionada.strftime('%d %B %Y')
        appointment_time = request.POST['appointment_time']
        
        try:
            # Convierte la hora de AM/PM a 24 horas
            appointment_time_24hr = datetime.strptime(appointment_time, "%I:%M %p").strftime("%H:%M")
        except ValueError:
            # Si la conversión falla, maneja el error (puedes devolver un mensaje al usuario o dejarla vacía)
            appointment_time_24hr = None
            
        your_mensaje = request.POST['your_mensaje']
        
        # Crear una nueva instancia del modelo Appointment
        appointment = Appointment(
            appointment_service=service_instance,  # Asignamos la instancia de Service
            appointment_doctor=doctor_instance,  # Asignamos la instancia de Dentist
            appointment_name=your_name,
            appointment_email=your_email,
            appointment_phone=your_phone,
            appointment_address=your_address,
            appointment_city=your_city,
            appointment_country=your_country,
            appointment_date=fecha_seleccionada,  # Guardamos la fecha como un objeto datetime
            #appointment_time=appointment_time,  # Guardamos la hora
            appointment_time=appointment_time_24hr,  # Guardamos la hora en formato de 24 horas
            appointment_message=your_mensaje,
            appointment_status=False  # O True, según tu lógica
        )
        
        # Guardar el objeto Appointment en la base de datos
        appointment.save()
        
        
        #send email 
        """
        send_mail(
            'Make appointment with this information: ' + your_name, # subject
            your_name + " \n" + your_email + " \n" + your_phone + " \n" + your_address + " \n" + your_city + " \n" + your_country + " \n" + service_name + " \n" + doctor_name + " \n" + fecha_seleccionada.strftime('%A') + " \n" + appointment_date + " \n" + appointment_time + " \n" + your_mensaje, # message
            your_email, # from email
            ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com'], # to email
        )
        """
        # Asunto del correo
        subject = 'Make appointment with this information: ' + your_name

        # Cuerpo del mensaje, añadiendo texto explicativo para cada campo
        """ message = (
            f"Name: {your_name} \n"
            f"Email: {your_email} \n"
            f"Phone: {your_phone} \n"
            f"Address: {your_address} \n"
            f"City: {your_city} \n"
            f"Country: {your_country} \n"
            f"Service: {service_name} \n"
            f"Doctor: {doctor_name} \n"
            f"Appointment Date: {appointment_date} \n"
            f"Appointment Time: {appointment_time} \n"
            f"Message: {your_mensaje}"
        ) """
        message = (
            f"Name: {your_name}\n"
            f"Email: {your_email}\n"
            f"Phone: {your_phone}\n"
            f"Address: {your_address}\n"
            f"City: {your_city}\n"
            f"Country: {your_country}\n"
            f"Service: {service_instance.service_name if service_instance else 'Unknown'}\n"
            f"Doctor: {doctor_instance.nombre if doctor_instance else 'Unknown'}\n"
            f"Appointment Date: {fecha_formateada}\n"
            f"Appointment Time: {appointment_time_24hr}\n"
            f"Message: {your_mensaje}"
        )

        # Dirección de correo del remitente
        from_email = your_email

        # Lista de correos a los que se enviará el mensaje
        to_email = ['msb.tesla@gmail.com', 'msb.coin@gmail.com', 'msb.duck@gmail.com', 'msebti2@gmail.com']

        # Enviar el correo
        send_mail(
            subject,  # Asunto
            message,  # Cuerpo del mensaje
            from_email,  # Correo del remitente
            to_email  # Correos de destino
        )
        
        """ context={'your_name':your_name, 'service_name':service_name, 'doctor_name':doctor_name, 'appointment_date':appointment_date, 'appointment_time':appointment_time, 'your_mensaje':your_mensaje, 'your_email': your_email, 'fecha_seleccionada':fecha_seleccionada.strftime('%A'),'fecha_formateada':fecha_formateada, 'your_country':your_country, 'your_city':your_city , 'your_phone':your_phone, 'your_address':your_address} """
        context = {
            'your_name': your_name,
            'service_name': service_instance.service_name if service_instance else "Servicio no encontrado",
            'doctor_name': doctor_instance.nombre + '' + doctor_instance.apellido if doctor_instance else "Doctor no encontrado",
            'appointment_date': fecha_formateada,
            'appointment_time': appointment_time_24hr,
            'your_mensaje': your_mensaje,
            'your_email': your_email,
            'your_country': your_country,
            'your_city': your_city,
            'your_phone': your_phone,
            'your_address': your_address
        }
        return render(request, 'dentist_app/appointment_other.html',context)
    else:
        context = {'services':services, 'doctors':doctors}
        return render(request, 'dentist_app/appointment_other.html',context)
    


