from flask import Flask, render_template, request, jsonify
import pandas as pd
from predict import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener datos del formulario
        data = {
            'age': int(request.form['age']),
            'workclass': request.form['workclass'],
            'fnlwgt': int(request.form['fnlwgt']),
            'education': request.form['education'],
            'education_num': int(request.form['education_num']),
            'marital_status': request.form['marital_status'],
            'occupation': request.form['occupation'],
            'relationship': request.form['relationship'],
            'race': request.form['race'],
            'sex': request.form['sex'],
            'capital_gain': int(request.form['capital_gain']),
            'capital_loss': int(request.form['capital_loss']),
            'hours_per_week': int(request.form['hours_per_week']),
            'native_country': request.form['native_country']
        }
        
        # Crear DataFrame
        df = pd.DataFrame([data])
        
        # Hacer predicción
        result = predict(df)
        
        prediction = "Más de 50K" if result[0] == 1 else "50K o menos"
        
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
