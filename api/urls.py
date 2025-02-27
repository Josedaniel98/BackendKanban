from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.proyecto import ProyectoViewSet
from api.views.tarea import TareaViewSet
from api.views.comentario import ComentarioViewSet
from api.views.historial_actividad import HistorialActividadViewSet

# Configuración del enrutador
router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tareas', TareaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'historial', HistorialActividadViewSet)

# Definir las rutas de la aplicación
urlpatterns = [
    path('', include(router.urls)),
]