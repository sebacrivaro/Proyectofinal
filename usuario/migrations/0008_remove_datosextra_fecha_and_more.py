# Generated by Django 5.1.2 on 2024-11-20 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_alter_datosextra_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosextra',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='datosextra',
            name='nueva_imagen',
        ),
    ]
