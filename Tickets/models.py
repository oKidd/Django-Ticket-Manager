from django.db import models
from datetime import datetime, date

# Create your models here.
class Ticket(models.Model):
    MINIMA = 'Minima'
    MEDIA = 'Media'
    ALTA = 'Alta'
    opciones = [
        (MINIMA, 'Minima'),
        (MEDIA, 'Media'),
        (ALTA, 'Alta'),
    ]
    id = models.AutoField(primary_key=True)
    asunto = models.CharField(max_length=100)
    emisor = models.CharField(max_length=50, default='Usuario')
    gravedad = models.CharField(max_length=100, choices=opciones, default=MINIMA)
    estado = models.CharField(max_length=30, default="No Atendido")
    fecha = models.DateField(default=date.today())
    hora = models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.id()

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    Ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=1000)
    emisor = models.CharField(max_length=50)
    fecha = models.DateField(default=date.today())
    hora = models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
