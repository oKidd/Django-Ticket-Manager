from django.shortcuts import render, redirect
from Tickets.models import Ticket, Respuesta
from Tickets.forms import TicketForm, RespuestaForm


# Create your views here.
def index(request):
    tickets = Ticket.objects.all()

    na = tickets.filter(estado="No Atendido").count
    re = tickets.filter(estado="Respondido").count
    ce = tickets.filter(estado="Cerrado").count
    total = tickets.count
    data = {'tickets': tickets, 'na': na, 're': re, 'ce': ce, 'total': total}
    return render(request, 'index.html', data)

def filtro(request, tipo):
    na = Ticket.objects.filter(estado="No Atendido").count
    re = Ticket.objects.filter(estado="Respondido").count
    ce = Ticket.objects.filter(estado="Cerrado").count

    if tipo:
        try:
            tickets = Ticket.objects.filter(estado=tipo)
            total = tickets.count
        except:
            data = {'na': na, 're': re, 'ce': ce, 'tipo': tipo, 'total': 0}
            return render(request, 'filtro.html', data)

    data = {'tickets': tickets, 'na': na, 're': re, 'ce': ce, 'total': total, 'tipo': tipo}
    return render(request, 'filtro.html', data)

def addTicket(request):
    form = TicketForm()
    # uform = UserForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    data = {'form': form}
    return render(request, 'addTicket.html', data)

def viewTicket(request, id):
    ticket = Ticket.objects.get(id = id)
    respuestas = Respuesta.objects.all().filter(Ticket=id)
    data = {'ticket': ticket, 'respuestas': respuestas}
    return render(request, 'ticket.html', data)

def responseTicket(request, id):
    ticket = Ticket.objects.get(id = id)
    form = RespuestaForm(initial={'Ticket': ticket})
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            form.save()
            ticket.estado = "Respondido"
            ticket.save()
            return viewTicket(request, id)
    data = {'form': form, 'ticket': ticket}
    return render(request, 'addResponse.html', data)

def closeTicket(request, id):
    ticket = Ticket.objects.get(id = id)
    ticket.estado = "Cerrado"
    ticket.save()
    return viewTicket(request, id)

def deleteTicket(request, id):
    ticket = Ticket.objects.get(id = id)
    ticket.delete()
    return redirect('/')