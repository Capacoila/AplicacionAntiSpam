from django.db import models
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from django.contrib.postgres.fields import ArrayField
from .training_utils import train_mensaje_model, train_llamada_model, get_categoria, get_precision
from rest_framework import viewsets, permissions
from .serializers import MensajeSerializer, LlamadaSerializer
from .models import Mensaje, Llamada



class Mensaje(models.Model):
    texto = models.CharField(max_length=200)
    clasificacion = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)

    def classify(self):
        # Cargar el modelo entrenado para mensajes
        with open('mensaje_model.pkl', 'rb') as file:
            vectorizer, clf = pickle.load(file)

        # Preprocesar el texto de entrada
        text_vectorized = vectorizer.transform([self.texto])

        # Realizar la clasificación
        self.clasificacion = clf.predict(text_vectorized)[0]

        # Obtener la categoría y precisión correspondiente a la clasificación
        self.categoria = get_categoria(self.clasificacion)  # Obtener la categoría según la clasificación
        self.precision = get_precision(self.clasificacion)  # Obtener la precisión según la clasificación

        # Guardar los cambios en el modelo
        self.save()

class Llamada(models.Model):
    numero = models.CharField(max_length=20)
    clasificacion = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)

    def classify(self):
        # Cargar el modelo entrenado para llamadas
        with open('llamada_model.pkl', 'rb') as file:
            vectorizer, clf = pickle.load(file)

        # Preprocesar el número de entrada
        number_vectorized = vectorizer.transform([self.numero])

        # Realizar la clasificación
        self.clasificacion = clf.predict(number_vectorized)[0]

        # Obtener la categoría y precisión correspondiente a la clasificación
        self.categoria = get_categoria(self.clasificacion)  # Obtener la categoría según la clasificación
        self.precision = get_precision(self.clasificacion)  # Obtener la precisión según la clasificación

        # Guardar los cambios en el modelo
        self.save()
