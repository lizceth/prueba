#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

GENERO=(
    ('M', 'Masculino'),
    ('F', 'Femenino'),
 )

class Usuario(User):
    nombre=models.CharField(max_length=40)
    apellido_pat=models.CharField(max_length=40)
    apellido_mat=models.CharField(max_length=40)
    sexo=models.CharField(max_length=1, choices=GENERO)
    E_mail=models.CharField(max_length=40)

    def __unicode__(self):
        return '%s %s' %(self.nombre, self.apellido_pat)

