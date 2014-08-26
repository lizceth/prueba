from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'fia.views.inicio'),
    url(r'^articulos/$', 'fia.views.articulos'),
    url(r'^agregar/articulo/$', 'fia.views.agregar_articulo'),
    url(r'^editar/articulo/(?P<id>\d+)$', 'fia.views.editar_articulo'),
    url(r'^borrar/articulo/(?P<id>\d+)$', 'fia.views.borrar_articulo'),
    url(r'^autores/$', 'fia.views.autores'),
    url(r'^detalle/(?P<id_articulo>\d+)$', 'fia.views.detalle'),
    url(r'^agregar/autor/$', 'fia.views.agregar_autor'),
    url(r'^editar/autor/(?P<id>\d+)$', 'fia.views.editar_autor'),
    url(r'^borrar/autor/(?P<id>\d+)$', 'fia.views.borrar_autor'),
    url(r'^comentario/$', 'fia.views.comentario'),
    url(r'^usuario/nuevo/$', 'fia.views.nuevo_usuario'),

    #aplicacion usuario
    url(r'^ingresar/$','usuarios.views.ingresar'),
    url(r'^privado/$','usuarios.views.privado'),
    url(r'^sesion/$','usuarios.views.index'),
    url(r'^cerrar/$','usuarios.views.cerrar'),
    url(r'^usuarios/$','usuarios.views.usuario'),
    url(r'^usuario/nuevo/$','usuarios.views.nuevo'),
    url(r'^editar/(?P<id>\d+)$','usuarios.views.editar'),
    url(r'^borrar/(?P<id>\d+)$','usuarios.views.borrar'),
)
