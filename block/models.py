from django.db import models

# Create your models here.
from django.db import models

from django.db import models
from django.contrib.postgres.fields import ArrayField
from .training_utils import train_mensaje_model, train_llamada_model

class Mensaje(models.Model):
    texto = models.CharField(max_length=200)
    clasificacion = models.CharField(max_length=20)
    categoria = models.CharField(max_length=100)
    precision = models.FloatField()

    def train_model(self):
        # Entrenar el modelo de mensajes
        train_mensaje_model()

class Llamada(models.Model):
    numero = models.CharField(max_length=20)
    clasificacion = models.CharField(max_length=20)
    categoria = models.CharField(max_length=100)
    precision = models.FloatField()

    def train_model(self):
        # Entrenar el modelo de llamadas
        train_llamada_model()

    