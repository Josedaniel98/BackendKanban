from rest_framework import serializers
from api.models import HistorialActividad

class HistorialActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialActividad
        fields = '__all__'