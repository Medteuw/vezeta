# Generated by Django 3.1.4 on 2020-12-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201226_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Specialist_doctor',
            field=models.CharField(blank=True, choices=[('Pediatre', 'Pediatre'), ('Medecin general', 'Medecin general'), ('Chirugien', 'Chirugien')], max_length=100, null=True, verbose_name='Specialite'),
        ),
    ]
