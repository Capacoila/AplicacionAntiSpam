import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def train_mensaje_model():
    # Cargar el conjunto de datos
    data = pd.read_csv("https://raw.githubusercontent.com/Capacoila/AplicacionAntiSpam/master/sms.tsv", sep='\t', header=None, names=['clasificacion', 'categoria', 'mensaje'])

    # Convertir las columnas 'clasificacion' y 'categoria' a tipo cadena
    data['clasificacion'] = data['clasificacion'].astype(str)
    data['categoria'] = data['categoria'].astype(str)

    # Preprocesar los datos
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['mensaje'])
    y = data['clasificacion']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar un modelo de Naive Bayes
    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    # Calcular la precisión en el conjunto de prueba
    y_pred = clf.predict(X_test)
    classification_accuracy = accuracy_score(y_test, y_pred)

    # Guardar el modelo entrenado
    with open('mensaje_model.pkl', 'wb') as file:
        pickle.dump((vectorizer, clf), file)

    return classification_accuracy

def train_llamada_model():
    # Cargar el conjunto de datos desde el archivo CSV
    data = pd.read_csv("https://raw.githubusercontent.com/Capacoila/AplicacionAntiSpam/master/Phone%20Number.tsv", delimiter="\t", header=None, names=['clasificacion', 'categoria', 'numero'])

    # Convertir la columna 'numero' a tipo cadena
    data['numero'] = data['numero'].astype(str)

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(data['numero'], data['clasificacion'], test_size=0.2, random_state=42)

    # Preprocesar los datos
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    # Entrenar un modelo de Naive Bayes
    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    # Calcular la precisión del modelo
    y_pred = clf.predict(X_test)
    classification_accuracy = accuracy_score(y_test, y_pred)

    # Guardar el modelo entrenado
    with open('llamada_model.pkl', 'wb') as file:
        pickle.dump((vectorizer, clf), file)

    return classification_accuracy

def load_test_data():
    # Cargar los datos de prueba para mensajes
    mensaje_data = pd.read_csv("https://raw.githubusercontent.com/Capacoila/AplicacionAntiSpam/master/sms_test.tsv", sep='\t', header=None, names=['clasificacion', 'categoria', 'mensaje'])
    X_mensaje_test = mensaje_data['mensaje']
    y_mensaje_true = mensaje_data['clasificacion']

    # Cargar los datos de prueba para llamadas
    llamada_data = pd.read_csv("https://raw.githubusercontent.com/Capacoila/AplicacionAntiSpam/master/Phone%20Number_test.tsv", delimiter="\t", header=None, names=['clasificacion', 'categoria', 'numero'])
    X_llamada_test = llamada_data['numero']
    y_llamada_true = llamada_data['clasificacion']

    return (X_mensaje_test, y_mensaje_true), (X_llamada_test, y_llamada_true)