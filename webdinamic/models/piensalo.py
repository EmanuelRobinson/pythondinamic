import random

# Calculadora lógica pura
def operacion_aritmetica(num1, num2, operacion):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if operacion == "/" and num2 == 0:
            return None, "No se puede dividir entre 0"
        resultado = eval(f"{num1} {operacion} {num2}")
        return resultado, None
    except ValueError:
        return None, "Error: Solo se aceptan números."

# Piedra papel o tijera
def juego_ppt(jugador):
    opciones = ["piedra", "papel", "tijera"]
    jugador = jugador.lower()

    if jugador not in opciones:
        return None, "Opción inválida. Debe ser piedra, papel o tijera."

    maquina = random.choice(opciones)
    if jugador == maquina:
        resultado = "¡Empate!"
    elif (jugador == "piedra" and maquina == "tijera") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijera" and maquina == "papel"):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"

    return f"EmaBoss eligió {maquina}. {resultado}", None

# Adivinar número (estado se guarda fuera)
def generar_numero_secreto():
    return random.randint(1, 10)

def evaluar_intento(numero_secreto, intento, intentos):
    try:
        intento = int(intento)
        intentos += 1

        if intento < 1 or intento > 10:
            return "Número fuera de rango (1 al 10)", intentos, False
        elif intento < numero_secreto:
            return "Muy bajo", intentos, False
        elif intento > numero_secreto:
            return "Muy alto", intentos, False
        else:
            return f"¡Correcto! Lo adivinaste en {intentos} intento(s).", intentos, True
    except ValueError:
        return "Entrada inválida. Usa solo números.", intentos, False
