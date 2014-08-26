from django.contrib import admin
from usuarios.models import Usuario
from django.contrib.auth.models import User

class UsuarioAdmin(admin.ModelAdmin):
    list_filter=['persona']
    list_display=['sexo','E_mail']

admin.site.register(Usuario)

