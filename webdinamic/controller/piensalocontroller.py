import random

numero_secreto = random.randint(1, 10)
intentos = 0

def calcular(num1, num2, operacion):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if operacion == '/' and num2 == 0:
            return None, "No se puede dividir entre 0"
        resultado = eval(f"{num1} {operacion} {num2}")
        return resultado, None
    except ValueError:
        return None, "Por favor ingresa solo números"

def jugar(jugador):
    opciones = ["piedra", "papel", "tijera"]
    jugador = jugador.lower()
    if jugador not in opciones:
        return "Opción inválida."

    maquina = random.choice(opciones)
    if jugador == maquina:
        return f"EmaBoss escogió {maquina}. ¡Empate!"
    elif (jugador == "piedra" and maquina == "tijera") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijera" and maquina == "papel"):
        return f"EmaBoss escogió {maquina}. ¡Ganaste!"
    else:
        return f"EmaBoss escogió {maquina}. ¡Perdiste!"

def adivinar(intento):
    global intentos, numero_secreto
    try:
        intento = int(intento)
        intentos += 1
        if intento < 1 or intento > 10:
            return "Debe ser un número entre 1 y 10."
        elif intento < numero_secreto:
            return "Muy bajo!"
        elif intento > numero_secreto:
            return "Muy alto!"
        else:
            msg = f"¡Correcto! Lo adivinaste en {intentos} intento(s)."
            numero_secreto = random.randint(1, 10)
            intentos = 0
            return msg
    except ValueError:
        return "Por favor, introduce un número válido."
