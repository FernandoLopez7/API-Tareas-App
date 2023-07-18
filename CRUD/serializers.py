from rest_framework import serializers
from .models import Tarea, TareaAsignada

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class TareaAsignadaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='tarea.nombre', read_only=True)
    class Meta:
        model = TareaAsignada
        fields = '__all__'