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

CATEGORIA=(
    ('Academico', 'Academico'),
    ('Tecnologico', 'Tecnologico'),
    ('Noticias', 'Noticias'),
    ('Deportes', 'Deportes'),
    ('Espiritual', 'Espiritual'),
    ('Social', 'Social'),

)

class Articulo(models.Model):
    autor=models.ForeignKey(Usuario)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_pub=models.DateTimeField(auto_now_add=True)
    categoria=models.CharField(max_length=11, choices=CATEGORIA)
    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering=['fecha_pub']

class Comentario(models.Model):
    articulo=models.ForeignKey(Articulo)
    comentario=models.TextField()
    fecha=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['fecha']
