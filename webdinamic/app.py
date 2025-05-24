"archivo principal para ejecutar el flask"

from flask import Flask, render_template, request, redirect, url_for
from controller.piensalocontroller import jugar, calcular, adivinar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    error = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operacion = request.form.get('operacion')
        resultado, error = calcular(num1, num2, operacion)
    return render_template('calculadora.html', resultado=resultado, error=error)

@app.route('/piedrapapeltijera', methods=['GET', 'POST'])
def piedrapapeltijera():
    resultado = None
    if request.method == 'POST':
        jugador = request.form.get('jugador')
        resultado = jugar(jugador)
    return render_template('piedrapapeltijera.html', resultado=resultado)

@app.route('/adivinar', methods=['GET', 'POST'])
def adivinar_numero():
    mensaje = None
    if request.method == 'POST':
        intento = request.form.get('intento')
        mensaje = adivinar(intento)
    return render_template('adivina.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

