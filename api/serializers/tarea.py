from rest_framework import serializers
from api.models import Tarea
from api.serializers.comentario import ComentarioSerializer 
from api.serializers.historial_actividad import HistorialActividadSerializer

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class TareasTableroSerializer(serializers.ModelSerializer):
    usuario_asignado = serializers.StringRelatedField()
    comentarios = serializers.SerializerMethodField()
    historial_actividad = serializers.SerializerMethodField()

    class Meta:
        model = Tarea
        fields = '__all__'

    def get_comentarios(self, obj):
        comentarios = obj.comentarios.all()
        return ComentarioSerializer(comentarios, many=True).data

    def get_historial_actividad(self, obj):
        historial_actividad = obj.historial.all()
        return HistorialActividadSerializer(historial_actividad, many=True).data
