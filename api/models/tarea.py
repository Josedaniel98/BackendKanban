from django.db import models
from django.contrib.auth.models import User
from .proyecto import Proyecto

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)

    usuario_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.titulo
