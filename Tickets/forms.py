from django import forms
from Tickets.models import Ticket, Respuesta

class TicketForm(forms.ModelForm):
    MINIMA = 'Minima'
    MEDIA = 'Media'
    ALTA = 'Alta'
    opciones = (
        (MINIMA, 'Minima'),
        (MEDIA, 'Media'),
        (ALTA, 'Alta'),
    )
    class Meta:
        model = Ticket
        fields = ('asunto', 'emisor','gravedad', 'descripcion')
    
    asunto = forms.CharField(max_length=100, widget=forms.TextInput({'class': 'form-control'}))
    emisor = forms.CharField(max_length=50, label="Tu nombre", widget=forms.TextInput({'class': 'form-control'}))
    gravedad = forms.ChoiceField(choices=opciones, widget=forms.Select({'class': 'form-select'}))
    descripcion = forms.CharField(max_length=1000, widget=forms.Textarea({'rows': '8', 'class': 'form-control'}))

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ('Ticket', 'emisor', 'descripcion')
    
    Ticket = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Ticket.objects.all())
    descripcion = forms.CharField(max_length=1000, label="Respuesta", widget=forms.Textarea({'rows': '8', 'class': 'form-control'}))
    emisor = forms.CharField(max_length=50, label="Tu nombre", widget=forms.TextInput({'class': 'form-control'}))
    
    


# class UserForm(forms.Form):
#     nombre = forms.CharField(max_length=30, widget=forms.TextInput({'class': 'form-control'}))
#     apellido = forms.CharField(max_length=30, widget=forms.TextInput({'class': 'form-control'}))
#     rut = forms.CharField(max_length=9, widget=forms.TextInput({'class': 'form-control'}))
#     fecha_nacimiento = forms.DateField(widget=forms.TextInput({'class': 'form-control', 'type': 'date'}))
#     email = forms.EmailField(widget=forms.TextInput({'class': 'form-control', 'type': 'email'}))
#     telefono = forms.CharField(max_length=9, widget=forms.TextInput({'class': 'form-control'}))
#     region = forms.CharField(max_length=40, widget=forms.TextInput({'class': 'form-control'}))
#     provincia = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
#     comuna = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
#     calle = forms.CharField(max_length=100, widget=forms.TextInput({'class': 'form-control'}))