# coding:utf-8
from django.forms import ModelForm
from django import forms
from fia.models import Articulo, Usuario, Comentario

class ArticuloForm(ModelForm):
     class Meta:
         model = Articulo

class UsuarioForm(ModelForm):
     class Meta:
         model = Usuario

class ComentarioForm(ModelForm):
     class Meta:
         model = Comentario
