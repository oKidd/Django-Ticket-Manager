from django.contrib import admin
from Tickets.models import Ticket, Respuesta

# Register your models here.
class AdminTicket(admin.ModelAdmin):
    list_display = ('asunto','gravedad', 'estado', 'descripcion')

admin.site.register(Ticket, AdminTicket)

class AdminResponse(admin.ModelAdmin):
    list_display = ('Ticket', 'emisor', 'descripcion')

admin.site.register(Respuesta, AdminResponse)