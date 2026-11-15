from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from menu.models import Categoria, Ingrediente, Plato


@login_required
def home(request):
    return render(request, 'menu/home.html', {
        'total_platos': Plato.objects.count(),
        'total_disponibles': Plato.objects.filter(disponible=True).count(),
        'total_categorias': Categoria.objects.count(),
        'total_ingredientes': Ingrediente.objects.count(),
    })
