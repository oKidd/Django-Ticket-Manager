# Generated by Django 4.1.1 on 2022-12-26 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0022_alter_respuesta_hora_alter_ticket_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='hora',
            field=models.TimeField(default='19:36:06'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora',
            field=models.TimeField(default='19:36:06'),
        ),
    ]
