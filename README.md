#INTEGRANTES: 

- Christopher Bazurto
- Alisson Caiza 


# Predictor de Ingresos

Este proyecto es una aplicación web que utiliza un modelo de aprendizaje automático para predecir si el ingreso de una persona es superior o inferior a 50K al año basándose en varios factores socioeconómicos.

## Características

- Modelo de árbol de decisión entrenado con datos socioeconómicos
- Interfaz web para ingresar datos y obtener predicciones
- Implementado con Flask

## Requisitos

- Python 3.8+
- Flask
- pandas
- scikit-learn
- joblib

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/predictor-ingresos.git
   cd predictor-ingresos
2. Importamos librerias
   ```bash
   import pandas as pd
      rom sklearn.model_selection import train_test_split, GridSearchCV
      from sklearn.preprocessing import OneHotEncoder, StandardScaler
      from sklearn.tree import DecisionTreeClassifier, plot_tree
      from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, roc_auc_score
      import matplotlib.pyplot as plt
      import seaborn as sns
      import numpy as np
      from sklearn import svm
      import pickle
      import sklearn
      sklearn.__version__
3. Cargamos dataset
   
        pd.set_option('display.max_rows', None)
         pd.set_option('display.max_columns', None)
         df = pd.read_csv('/content/data_evaluacion.csv')
5. Renombrar las columnas para que sean más claras

         df.columns = [
             'age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
             'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
             'hours_per_week', 'native_country', 'income'
         ]

         print(df.info())

         print(df.info())
7. Dividir los datos en conjuntos de entrenamiento y prueba
   

         # Separa las características (X) y la variable objetivo (y)
         X = df.drop('income', axis=1)
         y = df['income']
         
         # Convertir la variable objetivo a binario
         y = y.apply(lambda x: 1 if x == '>50K' else 0)
         
         # Identifica las columnas categóricas y numéricas
         X_categorical = X.select_dtypes(include=['object'])
         X_numeric = X.select_dtypes(include=['int64'])
         
         # Convierte las columnas booleanas a valores numéricos
         for col in X_categorical:
             if X_categorical[col].isin([True, False]).all():
                 X_categorical[col] = X_categorical[col].astype(int)

9. Guardar el modelo en el directorio

