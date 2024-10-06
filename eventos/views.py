from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Usuario, RegistroEvento
from .forms import EventoForm, RegistroEventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            return redirect('detalle_evento', evento_id=evento.id)
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    usuarios_registrados = evento.registroevento_set.all()
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'usuarios_registrados': usuarios_registrados})

def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

