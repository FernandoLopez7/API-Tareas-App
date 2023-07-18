from django.db import models
from django.contrib.auth.models import User

class GruposUsuarioTareas(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'GruposUsuarioTareas'

class UsuarioTareas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GruposUsuarioTareas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'UsuarioTareas'

class Tarea(models.Model):
    usuario = models.ForeignKey(UsuarioTareas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    fecha_limite = models.DateField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'tarea'

class TareaAsignada(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    asignado_a = models.ManyToManyField(UsuarioTareas)
    mensaje = models.CharField(max_length=100, default="Nueva tarea")
    
    class Meta:
        db_table = 'tarea_asignada'