import datetime

from django.db import models
from django.utils import timezone

class Department(models.Model):
    department_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.department_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class JobPosition(models.Model):
    job_position_description = models.CharField(max_length=150, help_text="Descripción del Perfil de Puesto", verbose_name="Descripción del Nivel de Confidencialidad", blank=False, null=False, default='DIRECTOR')
    department_default = models.ForeignKey(Department, on_delete=models.CASCADE)
    activo = models.BooleanField(blank=False, null=False, default=True, editable=True, help_text='Estado Lógico del Registro (Activo|Inactivo)', verbose_name='Activo')

    class Meta:
        ordering = ('job_position_description', )
        verbose_name_plural = 'Perfiles de Puestos'
    
    def __str__(self):
        return u'%s-%s (%s)' % (self.department_default, self.jobposition_name, )

class Function(models.Model):
    function = models.ForeignKey(Department, on_delete=models.CASCADE)
    function = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    function_name = models.CharField(max_length=200)

    def __str__(self):
        return self.function_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
