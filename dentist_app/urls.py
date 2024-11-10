"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('price.html', views.price, name="price"),
    path('service.html', views.service, name="service"),
    path('appointment.html', views.appointment, name="appointment"),
    path('team.html', views.team, name="team"),
    path('testimonial.html', views.testimonial, name="testimonial"),
    path('appointment_other.html', views.appointment_other, name="appointment_other"),
    #path('login.html', views.login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('dentist_form/', views.dentist_form_view, name='dentist_form'),
    path('dentist_admin/', views.dentist_admin_view, name='dentist_admin'),
    path('appointment_form/', views.appointment_form_view, name='appointment_form'),
    path('pricing_form/', views.pricing_form_view, name='pricing_form'),
    path('service_form/', views.service_form_view, name='service_form'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('actualizar_appointment/<id_appointment>', views.actualizar_appointment, name='actualizar_appointment'),
    path('eliminar_appointment/<id_appointment>', views.eliminar_appointment, name='eliminar_appointment'),
    path('contacts_list/', views.contacts_list_view, name='contacts_list'),
     path('actualizar_contacto/<id_contacto>', views.actualizar_contacto, name='actualizar_contacto'),
    path('eliminar_contacto/<id_contacto>', views.eliminar_contacto, name='eliminar_contacto'),
    path('newsletter/', views.newsletter, name='newsletter'),

]
