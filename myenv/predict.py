import pandas as pd
import joblib

# Cargar el modelo, el codificador y el escalador
model = joblib.load('decision_tree_model.joblib')
encoder = joblib.load('encoder.joblib')
scaler = joblib.load('scaler.joblib')

def preprocess_data(data):
    # Separar características categóricas y numéricas
    X_categorical = data.select_dtypes(include=['object'])
    X_numeric = data.select_dtypes(include=['int64'])
    
    # Aplicar codificación one-hot
    X_encoded = encoder.transform(X_categorical)
    
    # Escalar características numéricas
    X_numeric_scaled = scaler.transform(X_numeric)
    
    # Combinar características procesadas
    X_processed = pd.concat([pd.DataFrame(X_encoded), pd.DataFrame(X_numeric_scaled)], axis=1)
    
    return X_processed

def predict(input_data):
    # Preprocesar los datos de entrada
    processed_data = preprocess_data(input_data)
    
    # Realizar la predicción
    prediction = model.predict(processed_data)
    
    return prediction


