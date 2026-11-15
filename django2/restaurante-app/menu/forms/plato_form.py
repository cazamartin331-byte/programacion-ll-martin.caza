from django import forms
from django.utils import timezone

from menu.models import Plato


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['codigo', 'nombre', 'descripcion', 'precio', 'disponible',
                  'fecha_registro', 'categoria', 'ingredientes']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'precio': forms.NumberInput(attrs={'step': '0.01', 'min': '0.01'}),
            'fecha_registro': forms.DateInput(
                attrs={'type': 'date'}, format='%Y-%m-%d'),
            'ingredientes': forms.CheckboxSelectMultiple,
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if not nombre:
            raise forms.ValidationError('El nombre no puede estar vacío.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        return precio

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo'].strip().upper()
        if not (codigo.isascii() and codigo.isalnum() and 4 <= len(codigo) <= 6):
            raise forms.ValidationError(
                'El código debe tener entre 4 y 6 letras o números.')
        return codigo

    def clean_fecha_registro(self):
        fecha = self.cleaned_data['fecha_registro']
        if fecha > timezone.localdate():
            raise forms.ValidationError('La fecha no puede ser futura.')
        return fecha
