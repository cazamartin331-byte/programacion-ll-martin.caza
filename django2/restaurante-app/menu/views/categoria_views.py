from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from menu.forms import CategoriaForm
from menu.models import Categoria


@login_required
@permission_required('menu.view_categoria', raise_exception=True)
def categoria_list(request):
    return render(request, 'menu/categorias/list.html',
                  {'categorias': Categoria.objects.all()})


@login_required
@permission_required('menu.add_categoria', raise_exception=True)
def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría creada.')
        return redirect('categoria_list')
    return render(request, 'menu/categorias/form.html', {'form': form})


@login_required
@permission_required('menu.change_categoria', raise_exception=True)
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría actualizada.')
        return redirect('categoria_list')
    return render(request, 'menu/categorias/form.html', {'form': form})


@login_required
@permission_required('menu.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, 'Categoría eliminada.')
        except ProtectedError:
            messages.error(request, 'No se puede eliminar: tiene platos asociados.')
        return redirect('categoria_list')
    return render(request, 'menu/confirm_delete.html',
                  {'objeto': categoria, 'volver': 'categoria_list'})
