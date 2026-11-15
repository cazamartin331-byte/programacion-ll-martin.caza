from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm, MesaForm, ReservaForm
from .models import Cliente, Mesa, Reserva


def home(request):
    return render(request, 'reservas/home.html', {
        'total_mesas': Mesa.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'pendientes': Reserva.objects.filter(estado=Reserva.Estado.PENDIENTE).count(),
    })


def _crud(modelo, formulario, plantilla_lista, nombre, contexto):
    """Genera las 4 vistas CRUD sencillas de una entidad."""

    def lista(request):
        return render(request, plantilla_lista, {contexto: modelo.objects.all()})

    def crear(request):
        form = formulario(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, f'{nombre} creado.')
            return redirect(f'{contexto}_list')
        return render(request, 'reservas/form.html', {'form': form, 'titulo': f'Nuevo {nombre}'})

    def editar(request, pk):
        obj = get_object_or_404(modelo, pk=pk)
        form = formulario(request.POST or None, instance=obj)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, f'{nombre} actualizado.')
            return redirect(f'{contexto}_list')
        return render(request, 'reservas/form.html', {'form': form, 'titulo': f'Editar {nombre}'})

    def eliminar(request, pk):
        obj = get_object_or_404(modelo, pk=pk)
        if request.method == 'POST':
            obj.delete()
            messages.success(request, f'{nombre} eliminado.')
            return redirect(f'{contexto}_list')
        return render(request, 'reservas/confirm_delete.html',
                      {'objeto': obj, 'volver': f'{contexto}_list'})

    return lista, crear, editar, eliminar


mesas_list, mesas_create, mesas_update, mesas_delete = _crud(
    Mesa, MesaForm, 'reservas/mesas.html', 'Mesa', 'mesas')
clientes_list, clientes_create, clientes_update, clientes_delete = _crud(
    Cliente, ClienteForm, 'reservas/clientes.html', 'Cliente', 'clientes')


def reservas_list(request):
    estado = request.GET.get('estado', '')
    reservas = Reserva.objects.select_related('mesa', 'cliente')
    if estado in Reserva.Estado.values:
        reservas = reservas.filter(estado=estado)
    return render(request, 'reservas/reservas.html', {
        'reservas': reservas, 'estado': estado, 'estados': Reserva.Estado.choices})


def reservas_create(request):
    form = ReservaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Reserva creada.')
        return redirect('reservas_list')
    return render(request, 'reservas/form.html', {'form': form, 'titulo': 'Nueva reserva'})


def reservas_update(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    form = ReservaForm(request.POST or None, instance=reserva)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Reserva actualizada.')
        return redirect('reservas_list')
    return render(request, 'reservas/form.html', {'form': form, 'titulo': 'Editar reserva'})


def reservas_delete(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada.')
        return redirect('reservas_list')
    return render(request, 'reservas/confirm_delete.html',
                  {'objeto': reserva, 'volver': 'reservas_list'})
