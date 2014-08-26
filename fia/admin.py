from django.contrib import admin
from django.contrib.auth.models import User
from fia.models import Usuario, Articulo, Comentario

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['nombre','apellido_pat','apellido_mat','sexo','E_mail']

class ArticuloAdmin(admin.ModelAdmin):
    list_display=['titulo','contenido','fecha_pub','categoria']

class ComentarioAdmin(admin.ModelAdmin):
    list_display=['comentario','fecha']
    list_filter=['articulo']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)
