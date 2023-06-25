from .models import Mensaje, Llamada
from rest_framework import viewsets, permissions
from .serializers import MensajeSerializer, LlamadaSerializer
from .training_utils import train_mensaje_model, train_llamada_model

from rest_framework import viewsets
from .models import Mensaje, Llamada
from .serializers import MensajeSerializer, LlamadaSerializer

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MensajeSerializer

    def perform_create(self, serializer):
        mensaje = serializer.save()
        mensaje.classify()
        serializer.instance = mensaje

    def perform_update(self, serializer):
        mensaje = serializer.save()
        mensaje.classify()
        serializer.instance = mensaje

class LlamadaViewSet(viewsets.ModelViewSet):
    queryset = Llamada.objects.all()
    serializer_class = LlamadaSerializer

    def perform_create(self, serializer):
        llamada = serializer.save()
        llamada.classify()
        serializer.instance = llamada

    def perform_update(self, serializer):
        llamada = serializer.save()
        llamada.classify()
        serializer.instance = llamada
