# Generated by Django 5.1.2 on 2024-11-16 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist_app', '0005_serviceimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DentistImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dentist_image_description', models.TextField(verbose_name='Descripción')),
                ('dentist_image_image', models.ImageField(upload_to='dentists/', verbose_name='Imagen')),
                ('dentist_image_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dentist_app.dentist')),
            ],
        ),
    ]