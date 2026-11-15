from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from menu.forms import PlatoForm
from menu.models import Categoria, Plato


@login_required
@permission_required('menu.view_plato', raise_exception=True)
def plato_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria', '').strip()

    platos = (Plato.objects
              .select_related('categoria')
              .prefetch_related('ingredientes'))
    if pista:
        platos = platos.filter(
            Q(nombre__icontains=pista)
            | Q(codigo__icontains=pista)
            | Q(ingredientes__nombre__icontains=pista)
            | Q(categoria__nombre__icontains=pista)
        ).distinct()
    if categoria_id.isdigit():
        platos = platos.filter(categoria_id=int(categoria_id))

    return render(request, 'menu/platos/list.html', {
        'platos': platos,
        'categorias': Categoria.objects.all(),
        'pista': pista,
        'categoria_id': categoria_id,
    })


@login_required
@permission_required('menu.add_plato', raise_exception=True)
def plato_create(request):
    form = PlatoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Plato creado.')
        return redirect('plato_list')
    return render(request, 'menu/platos/form.html', {'form': form})


@login_required
@permission_required('menu.change_plato', raise_exception=True)
def plato_update(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    form = PlatoForm(request.POST or None, instance=plato)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Plato actualizado.')
        return redirect('plato_list')
    return render(request, 'menu/platos/form.html', {'form': form})


@login_required
@permission_required('menu.delete_plato', raise_exception=True)
def plato_delete(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == 'POST':
        plato.delete()
        messages.success(request, 'Plato eliminado.')
        return redirect('plato_list')
    return render(request, 'menu/confirm_delete.html',
                  {'objeto': plato, 'volver': 'plato_list'})
