from django.db import models
from django.contrib.auth.models import User
from .tarea import Tarea

class HistorialActividad(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name="historial")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()  # Ejemplo: "Cambiado de 'Pendiente' a 'En Progreso'"
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tarea.titulo} - {self.descripcion} ({self.fecha})"