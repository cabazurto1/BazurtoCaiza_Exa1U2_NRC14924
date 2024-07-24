## INTEGRANTES: 

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
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # En Windows usa: myenv\Scripts\activate
3. Instala las dependencias:
    ```bash
        pip install -r requirements.txt
## Uso
1. Ejecuta la aplicación:

   ```bash
   python app.py
2. Abre un navegador y ve a http://127.0.0.1:5000/

3. Llena el formulario con los datos requeridos y haz clic en "Predecir" para obtener una predicción.

## Estructura del Proyecto
   - app.py: Aplicación principal de Flask
   - predict.py: Contiene la lógica de predicción y carga del modelo
   - templates/: Contiene las plantillas HTML
   - decision_tree_model.joblib: Modelo de árbol de decisión entrenado
   - encoder.joblib: Codificador para variables categóricas
   - scaler.joblib: Escalador para variables numéricas
## Copyright (c) [2024] [Christopher Bazurto & Alisson Caiza ]
