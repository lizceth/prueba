from django.shortcuts import render, render_to_response, get_object_or_404
from fia.models import Articulo,Usuario, Comentario
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from fia.forms import ArticuloForm,  ComentarioForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def inicio(request):
    articulos=Articulo.objects.order_by('fecha_pub')
    return render_to_response('fia/inicio.html',
                              {'articulos':articulos},
                          context_instance=RequestContext(request))

def articulos(request):
    articulos=Articulo.objects.all()
    return render_to_response('fia/articulo.html',
                          {'articulos':articulos},
                          context_instance=RequestContext(request))

def detalle(request, id_articulo):
    articulo = get_object_or_404(Articulo, id=id_articulo)
    comentario=Comentario.objects.filter(articulo=articulo)
    return render(request, 'fia/detalle.html',
                  {'articulo':articulo, 'comentario':comentario})


def agregar_articulo(request):
    if request.method == 'POST':
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/articulos/')
    else:
        formulario = ArticuloForm()
    return render_to_response('fia/articuloform.html',
                              {'formulario':formulario},
                          context_instance=RequestContext(request))


def editar_articulo (request, id):
        editar_articulo= Articulo.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ArticuloForm(request.POST, instance = editar_articulo)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/articulos/")
        else:
            formulario = ArticuloForm(instance= editar_articulo)
        return render_to_response('fia/articulo_edit.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))

def borrar_articulo (request, id):
    borrar_articulo = get_object_or_404(Articulo, pk=id)
    borrar_articulo.delete()
    return HttpResponseRedirect("/articulos/")


def autores(request):
    autores=Autor.objects.all()
    return render_to_response('fia/autores.html',
                              {'autores':autores},
                          context_instance=RequestContext(request))

def agregar_autor(request):
    if request.method == 'POST':
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/autores/')
    else:
        formulario = AutorForm()
    return render_to_response('fia/autorform.html',
                              {'formulario':formulario},
                          context_instance=RequestContext(request))


def editar_autor (request, id):
        editar_autor= Autor.objects.get(pk=id)
        if request.method == 'POST':
            formulario = AutorForm(request.POST, instance = editar_autor)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/autores/")
        else:
            formulario = AutorForm(instance= editar_autor)
        return render_to_response('fia/editar_autor.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))

def borrar_autor (request, id):
    borrar_autor = get_object_or_404(Autor, pk=id)
    borrar_autor.delete()
    return HttpResponseRedirect("/autores/")

def comentario(request):
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/")
    else:
        formulario = ComentarioForm()
    return render_to_response('fia/comentarioform.html',
                              {'formulario': formulario},
                              context_instance=RequestContext(request))
