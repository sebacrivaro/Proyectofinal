# Generated by Django 5.1.2 on 2024-11-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='deporte_fav',
            field=models.CharField(default='basquet', max_length=20),
        ),
        migrations.AddField(
            model_name='datosextra',
            name='edad',
            field=models.IntegerField(default=23),
        ),
        migrations.AddField(
            model_name='datosextra',
            name='equipo_fav',
            field=models.CharField(default='lakers', max_length=20),
        ),
    ]
