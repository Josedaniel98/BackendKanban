from rest_framework import viewsets
from api.models import Proyecto
from api.serializers import ProyectoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer