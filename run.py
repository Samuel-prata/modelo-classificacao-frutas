from flask import Flask, render_template, request
import pandas as pd
import joblib

# Carregar modelo
modelo = joblib.load('classificacao_knn_frutas.joblib')

# Nome das frutas
nomes = ['Maçã', 'Laranja', 'Limão']

# Iniciar app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    try:
        peso = float(request.form['peso'])
        diametro = float(request.form['diametro'])
        entrada = [[peso, diametro]]
        resultado = modelo.predict(entrada)
        fruta = nomes[resultado[0]]
        return render_template('index.html', resultado=f'Fruta prevista: {fruta}')
    except Exception as e:
        return render_template('index.html', resultado=f'Erro: {e}')

if __name__ == '__main__':
    app.run(debug=True)
