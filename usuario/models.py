from tabnanny import verbose
from django.db import models
from django.forms import IntegerField
from numpy import False_
from sympy import Max

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    cedula = models.IntegerField(blank = True, null = True)
    nombres = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 100, blank = False, null = False)
    descripcion = models.TextField(blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    estado = models.BooleanField('Estado', default = True)

    

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def natural_key(self):
        return f'{self.nombres} {self.apellidos}'

    def __str__(self):
        return self.nombres

categoria = [
    (1, 'Tesis'),
    (2, 'Articulo'),
    (3, 'Monografia')
]

class Documento(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 255, blank =  False, null = False)
    resumen = models.TextField(max_length=255, blank = True, null = True)
    fecha_publicacion = models.DateTimeField('Fecha de publicación', blank = False, null = False)
    Usuario_id = models.ManyToManyField(Usuario)
    palabras_clave = models.TextField(max_length= 100, blank =True, null = True)
    tipo_producto = models.IntegerField(null=False, blank = False, choices=categoria, default=1)
    archivo = models.FileField(upload_to='archivos/', max_length=255, blank = True, null= True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    estado = models.BooleanField(default = True, verbose_name = 'name')
                                
    class Meta: 
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo



