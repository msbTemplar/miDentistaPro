# Generated by Django 5.1.2 on 2024-11-10 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.CharField(max_length=2000)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Service Price')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_name', models.CharField(max_length=200, verbose_name='Name')),
                ('appointment_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('appointment_phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('appointment_address', models.CharField(max_length=500, verbose_name='Address')),
                ('appointment_city', models.CharField(max_length=200, verbose_name='City')),
                ('appointment_country', models.CharField(max_length=200, verbose_name='Country')),
                ('appointment_date', models.DateField(verbose_name='Appointment Date')),
                ('appointment_time', models.DateField(verbose_name='Appointment Time')),
                ('appointment_message', models.CharField(max_length=2000, verbose_name='Message')),
                ('appointment_status', models.BooleanField(default=False, verbose_name='Set/Not?')),
                ('appointment_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dentist_app.dentist')),
                ('appointment_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dentist_app.service')),
            ],
        ),
    ]
