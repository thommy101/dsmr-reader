# Generated by Django 2.0.9 on 2018-11-14 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_frontend', '0014_phases_currently_returned'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'default_permissions': (), 'verbose_name': 'Application notification'},
        ),
    ]