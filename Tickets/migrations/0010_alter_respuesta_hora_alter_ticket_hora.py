# Generated by Django 4.1.1 on 2022-12-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0009_alter_respuesta_hora_alter_ticket_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='hora',
            field=models.TimeField(default='05:11:19'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora',
            field=models.TimeField(default='05:11:19'),
        ),
    ]
