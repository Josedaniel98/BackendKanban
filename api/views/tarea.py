from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Tarea
from api.serializers import TareaSerializer, TareasTableroSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    @action(detail=False, methods=['get'], url_path='tablero')
    def tablero(self, request, *args, **kwargs):
        queryset = Tarea.objects.all()
        params = request.query_params
        if params.get('proyecto_id', None) is not None:
            queryset = queryset.filter(proyecto_id=params.get('proyecto_id'))
        if params.get('usuario_asignado_id', None) is not None:
            queryset = queryset.filter(usuario_asignado_id=params.get('usuario_asignado_id'))
        if params.get('estado', None) is not None:
            queryset = queryset.filter(estado=params.get('estado'))
        serializer = TareasTableroSerializer(queryset, many=True)
        return Response(serializer.data)