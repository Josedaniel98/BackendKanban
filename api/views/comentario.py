from rest_framework import viewsets
from api.models import Comentario
from api.serializers import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer