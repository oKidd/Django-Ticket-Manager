# Generated by Django 4.1.1 on 2022-12-26 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0020_alter_respuesta_hora_alter_ticket_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='Ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tickets.ticket'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='hora',
            field=models.TimeField(default='19:08:06'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hora',
            field=models.TimeField(default='19:08:06'),
        ),
    ]
