import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from django.db import models
from django.contrib.postgres.fields import ArrayField
from sklearn.metrics import precision_score
from .training_utils import load_test_data, load_categorias_data
from sklearn.metrics import precision_score


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
        text_vectorized = vectorizer.transform([str(self.texto)])

        # Realizar la clasificación
        self.clasificacion = clf.predict(text_vectorized)[0]

        # Obtener la categoría basada en la clasificación (agrega la lógica adecuada)
        categorias_mensaje, _ = load_categorias_data()

        # Asignar la categoría basada en la clasificación
        if self.clasificacion == 'nospam':
          self.categoria = categorias_mensaje[0]
        else:
         self.categoria = categorias_mensaje[1] if categorias_mensaje[1] != 'General' else categorias_mensaje[2]


        # Obtener los datos de prueba y las etiquetas verdaderas correspondientes
        X_mensaje_test, y_mensaje_true, _, _, = load_test_data()

        # Preprocesar los datos de prueba
        X_test_vectorized = vectorizer.transform(X_mensaje_test)

        # Realizar la clasificación en los datos de prueba
        y_pred = clf.predict(X_test_vectorized)

        # Calcular la precisión
        self.precision = precision_score(y_mensaje_true, y_pred, pos_label='spam') if self.clasificacion == 'spam' else precision_score(y_mensaje_true, y_pred, pos_label='nospam')
        
    


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
        number_vectorized = vectorizer.transform([str(self.numero)])

        # Realizar la clasificación
        self.clasificacion = clf.predict(number_vectorized)[0]

        # Obtener las categorías correspondientes
        _, categorias_llamada = load_categorias_data()

       # Asignar la categoría basada en la clasificación
        if self.clasificacion == 'spam':
         self.categoria = categorias_llamada[1]
        else:
         self.categoria = categorias_llamada[0]

        # Obtener los datos de prueba y las etiquetas verdaderas correspondientes
        _, _, X_llamada_test, y_llamada_true = load_test_data()

        # Preprocesar los datos de prueba
        X_test_vectorized = vectorizer.transform(X_llamada_test)

        # Realizar la clasificación en los datos de prueba
        y_pred = clf.predict(X_test_vectorized)

        # Calcular la precisión
        self.precision = precision_score(y_llamada_true, y_pred, pos_label='spam') if self.clasificacion == 'spam' else precision_score(y_llamada_true, y_pred, pos_label='nospam')
    


        # Guardar los cambios en el modelo
        self.save()

