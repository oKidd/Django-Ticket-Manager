# Generated by Django 4.1.1 on 2022-12-15 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0006_respuesta_rename_fecha_creacion_ticket_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='hora',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]