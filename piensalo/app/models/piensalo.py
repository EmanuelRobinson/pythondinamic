import random

def jugar_ppt(jugador):
    opciones = ["piedra", "papel", "tijera"]
    if jugador not in opciones:
        return "Error", "No tiene sentido lo que colocas jajaj.", None
    maquina = random.choice(opciones)
    if jugador == maquina:
        resultado = "DIOS! es un Empate"
    elif (jugador == "piedra" and maquina == "tijera") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijera" and maquina == "papel"):
        resultado = "Tan pro!? Ganaste mi rey."
    else:
        resultado = "Suerte a la prox panita."
    return jugador, resultado, maquina

def calcular(num1, num2, operacion):
    if operacion == "/" and num2 == 0:
        return "Error: no se puede dividir entre 0."
    try:
        return eval(f"{num1} {operacion} {num2}")
    except:
        return "Error en operación."

def generar_numero_secreto():
    return random.randint(1, 10)

def verificar_adivinanza(intentado, secreto):
    if intentado < 1 or intentado > 10:
        return "Bro, es del 1 al 10 no más xdd."
    elif intentado < secreto:
        return "Muy bajito!"
    elif intentado > secreto:
        return "Te pasaste xd!"
    else:
        return f"Lo lograste. El número era {secreto}!"
