from rest_framework import viewsets
from api.models import HistorialActividad
from api.serializers import HistorialActividadSerializer

class HistorialActividadViewSet(viewsets.ModelViewSet):
    queryset = HistorialActividad.objects.all()
    serializer_class = HistorialActividadSerializer
    