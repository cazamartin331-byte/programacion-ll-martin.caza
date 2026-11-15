from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from menu.forms import IngredienteForm
from menu.models import Ingrediente


@login_required
@permission_required('menu.view_ingrediente', raise_exception=True)
def ingrediente_list(request):
    return render(request, 'menu/ingredientes/list.html',
                  {'ingredientes': Ingrediente.objects.all()})


@login_required
@permission_required('menu.add_ingrediente', raise_exception=True)
def ingrediente_create(request):
    form = IngredienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Ingrediente creado.')
        return redirect('ingrediente_list')
    return render(request, 'menu/ingredientes/form.html', {'form': form})


@login_required
@permission_required('menu.change_ingrediente', raise_exception=True)
def ingrediente_update(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    form = IngredienteForm(request.POST or None, instance=ingrediente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Ingrediente actualizado.')
        return redirect('ingrediente_list')
    return render(request, 'menu/ingredientes/form.html', {'form': form})


@login_required
@permission_required('menu.delete_ingrediente', raise_exception=True)
def ingrediente_delete(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    if request.method == 'POST':
        ingrediente.delete()
        messages.success(request, 'Ingrediente eliminado.')
        return redirect('ingrediente_list')
    return render(request, 'menu/confirm_delete.html',
                  {'objeto': ingrediente, 'volver': 'ingrediente_list'})
