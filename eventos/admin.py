from django.contrib import admin
from .models import Usuario, Evento, RegistroEvento

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha', 'organizador')

@admin.register(RegistroEvento)
class RegestroEventoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'fecha_registro')
