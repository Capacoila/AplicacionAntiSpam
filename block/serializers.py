from rest_framework import serializers
from .models import Llamada
from .models import Mensaje

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ('id', 'texto', 'clasificacion', 'categoria', 'precision')

class LlamadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llamada
        fields = ('id', 'numero', 'clasificacion', 'categoria', 'precision')
