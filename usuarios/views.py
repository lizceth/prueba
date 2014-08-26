from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from usuarios.models import Usuario

def index(request):
    titulo='inicio de secion'
    return render_to_response('usuarios/index.html',{'titulo':titulo}, context_instance=RequestContext(request))

def usuario(request):
    usuarios=User.objects.all()
    titulo='todos los usuarios'
    return render_to_response('usuarios/usuarios.html',
                              {'usuarios':usuarios,'titulo':titulo},
                              context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('usuarios/noactivo.html',
                                              context_instance=RequestContext(request))
            else:
                return render_to_response('usuarios/nousuario.html',
                                          context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('usuarios/ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/usuarios/')
    else:
        formulario = UserCreationForm()
    return render_to_response('usuarios/nuevo_usuario.html',
                              {'formulario':formulario}, context_instance=RequestContext(request))

def editar(request, id):
    editar=User.objects.get(pk=id)
    if request.method=='POST':
        formulario = UserCreationForm(request.POST, instance=editar)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/usuarios/')
    else:
        formulario = UserCreationForm(instance=editar)
    return render_to_response('usuarios/editar_usuario.html',
                              {'formulario':formulario}, context_instance=RequestContext(request))


def borrar(request, id):
    borrar=get_object_or_404(User, pk=id)
    borrar.delete()
    return HttpResponseRedirect ("/usuarios/")

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('usuarios/privado.html',
                              {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
