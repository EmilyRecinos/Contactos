from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(TelefonoCliente)
admin.site.register(TipoTelefono)