from django import forms
from django.utils import timezone

from .models import Cliente, Mesa, Reserva


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidad', 'ubicacion']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono']


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'cliente', 'fecha', 'hora', 'personas', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'hora': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.localdate():
            raise forms.ValidationError('La fecha no puede estar en el pasado.')
        return fecha

    def clean(self):
        datos = super().clean()
        mesa, personas = datos.get('mesa'), datos.get('personas')
        if mesa and personas and personas > mesa.capacidad:
            self.add_error('personas', f'La mesa solo admite {mesa.capacidad} personas.')
        return datos
