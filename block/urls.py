from django.urls import include, path
from rest_framework import routers
from .api import MensajeViewSet, LlamadaViewSet

router = routers.DefaultRouter()
router.register('api/mensaje', MensajeViewSet, 'mensajes')
router.register('api/llamada', LlamadaViewSet, 'llamadas')

urlpatterns = router.urls


