from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

Activo = True
Inactivo = False

class nivelDeConfidencialidad(models.Model):
    descripcion_nivel_confidencialidad = models.CharField(max_length=50, help_text="Descripción del Nivel de Confidencialidad", verbose_name="Descripción del Nivel de Confidencialidad", blank=False, null=False, default=None)
    nivel_confidencialidad = models.IntegerField(default=0, validators=[MaxValueValidator(100),MinValueValidator(0)], help_text="100 - Mayor de Nivel de Acceso, 0 - Nulo nivel de acceso", verbose_name="Nivel de Confidencialidad")
    activo = models.BooleanField(default=Activo, help_text='Estado Lógico del Registro (Activo/Inactivo)', verbose_name='Activo', blank=False, null=False)

    def __str__(self):
        return u'%s (%s)' % (self.descripcion_nivel_confidencialidad, self.nivel_confidencialidad)

    class Meta:
        ordering = ('nivel_confidencialidad','descripcion_nivel_confidencialidad',)
        verbose_name_plural = "Niveles de Confidencialidad"

class Departamento(models.Model):
    nombre = models.CharField('nombre', default='departamento', help_text='Departamento', unique=True, blank=False, null=False, max_length=200)
    nivel = models.CharField(max_length=4, default='1', null=False, blank=False)
    
    def __str__(self):
        return u'%s (%s)' % (self.nombre, self.nivel)

    class Meta:
        ordering = ('nivel', 'nombre')

class Area(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    area = models.CharField('area', default='area', help_text='Area', blank=False, null=False, max_length=200)

    def __str__(self):
        return self.departamento + self.area

class Puesto(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, default='Nombre del Puesto', null=False, blank=False, help_text="Puesto")
    
    def __str__(self):
        return self.departamento + self.area + self.nombre
    
class Funcion(models.Model):
    nombre = models.CharField(max_length=128)
    
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.TextField(max_length=150, default='Actividad')

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    curp = models.CharField(max_length=18, verbose_name='CURP')
    nombre = models.CharField(max_length=80, verbose_name='NOMBRE')
    paterno = models.CharField(max_length=80, verbose_name='APELLIDO PATERNO')
    materno = models.CharField(max_length=80, verbose_name='APELLIDO MATERNO')
    def __str__(self):
        return self.nombre + " " + self.paterno + " " + self.materno
