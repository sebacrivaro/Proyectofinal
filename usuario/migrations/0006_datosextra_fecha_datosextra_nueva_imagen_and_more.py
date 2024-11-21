# Generated by Django 5.1.2 on 2024-11-20 14:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_datosextra_deporte_fav_alter_datosextra_edad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='datosextra',
            name='nueva_imagen',
            field=models.ImageField(blank=True, null=True, upload_to='otra_foto'),
        ),
        migrations.AlterField(
            model_name='datosextra',
            name='deporte_fav',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='datosextra',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='datosextra',
            name='equipo_fav',
            field=models.CharField(max_length=20),
        ),
    ]