from app.models import piensalo

def jugar_ppt(jugador):
    return piensalo.jugar_ppt(jugador)

def realizar_calculo(num1, num2, operacion):
    return piensalo.calcular(num1, num2, operacion)

def generar_numero():
    return piensalo.generar_numero_secreto()

def verificar_numero(intentado, secreto):
    return piensalo.verificar_adivinanza(intentado, secreto)
