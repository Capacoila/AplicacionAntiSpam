import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from django.db import models
from django.contrib.postgres.fields import ArrayField
from sklearn.metrics import precision_score
from .training_utils import train_mensaje_model, train_llamada_model, load_test_data

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

        # Obtener la categoría basada en la clasificación (agrega la lógica adecuada)
        self.categoria = ""

        # Obtener los datos de prueba y las etiquetas verdaderas correspondientes
        X_test, y_true = load_test_data()  # Reemplaza con tu función para cargar los datos de prueba

        # Preprocesar los datos de prueba
        X_test_vectorized = vectorizer.transform(X_test)

        # Realizar la clasificación en los datos de prueba
        y_pred = clf.predict(X_test_vectorized)

        # Calcular la precisión
        self.precision = precision_score(y_true, y_pred)

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

        # Obtener la categoría basada en la clasificación (agrega la lógica adecuada)
        self.categoria = ""

        # Obtener los datos de prueba y las etiquetas verdaderas correspondientes
        X_test, y_true = load_test_data()  # Reemplaza con tu función para cargar los datos de prueba

        # Preprocesar los datos de prueba
        X_test_vectorized = vectorizer.transform(X_test)

        # Realizar la clasificación en los datos de prueba
        y_pred = clf.predict(X_test_vectorized)

        # Calcular la precisión
        self.precision = precision_score(y_true, y_pred)

        # Guardar los cambios en el modelo
        self.save()