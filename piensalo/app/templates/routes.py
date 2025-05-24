from flask import Blueprint, render_template, request
from app.controls import piensalocontroller as controller

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operacion = request.form['operacion']
        resultado = controller.realizar_calculo(num1, num2, operacion)
    return render_template('calculadora.html', resultado=resultado)

@routes.route('/piedrapapeltijera', methods=['GET', 'POST'])
def ppt():
    resultado = None
    jugador = None
    maquina = None
    if request.method == 'POST':
        jugador = request.form['jugador']
        jugador, resultado, maquina = controller.jugar_ppt(jugador)
    return render_template('piedra.html', resultado=resultado, jugador=jugador, maquina=maquina)

@routes.route('/adivinar', methods=['GET', 'POST'])
def adivinar():
    mensaje = None
    secreto = controller.generar_numero()
    if request.method == 'POST':
        secreto = int(request.form['secreto'])  # campo oculto
        intento = int(request.form['intento'])
        mensaje = controller.verificar_numero(intento, secreto)
    return render_template('adivinar.html', mensaje=mensaje, secreto=secreto)
