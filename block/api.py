from .models import Mensaje, Llamada
from rest_framework import viewsets, permissions
from .serializers import MensajeSerializer, LlamadaSerializer

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MensajeSerializer

class LlamadaViewSet(viewsets.ModelViewSet):
    queryset = Llamada.objects.all()
    serializer_class = LlamadaSerializer
    permission_classes = [permissions.AllowAny]