import random

operaciones = ["+", "-", "*", "/"]

def piedrapapeltijera(nombre):
    opciones = ["piedra", "papel", "tijera"]
    while True:
        jugador = input(f"{nombre}, escoge y escribe: piedra, papel o tijera: ").lower()
        if jugador == "salir":
            print("Nos vemos")
            break
        if jugador not in opciones:
            print("No tiene sentido lo que colocas jajaj.")
            continue
        maquina = random.choice(opciones)
        print(f"EmaBoss escogió..: {maquina}")
        
        if jugador == maquina:
            print("DIOS! es un Empate")
        elif (jugador == "piedra" and maquina == "tijera") or \
             (jugador == "papel" and maquina == "piedra") or \
             (jugador == "tijera" and maquina == "papel"):
            print("Tan pro!? Ganaste mi rey.")
        else:
            print("Suerte a la prox panita.")

def calculadora(nombre):
    while True:
        try:
            num1 = int(input(f"{nombre}, inserta número 1: "))
            num2 = int(input("Inserta número 2: "))
            
            operacion = input("Selecciona tu operación [+ - * /]: ")
            while operacion not in operaciones:
                operacion = input("Introduce una operación válida [+ - * /]: ")

            if operacion == "/" and num2 == 0:
                print("Error: no se puede dividir entre 0.")
            else:
                resultado = eval(f"{num1} {operacion} {num2}")
                print(f"{num1} {operacion} {num2} = {resultado}")
        
        except ValueError:
            print("Error: debes ingresar solo números.")
        
        repetir = input("¿Otra operación? (siu/nao): ").lower()
        if repetir != "siu":
            break

def adivinar_numero(nombre):
    print(f"{nombre}, estoy pensando en un número del 1 al 10. ¿Puedes adivinar cuál es?")
    numero_secreto = random.randint(1, 10)
    intentos = 0
    
    while True:
        try:
            intento = int(input("Tu número: "))
            intentos += 1
            
            if intento < 1 or intento > 10:
                print("Bro, es del 1 al 10 no más xdd.")
            elif intento < numero_secreto:
                print("Muy bajito!")
            elif intento > numero_secreto:
                print("Te pasaste xd!")
            else:
                print(f"Lo lograste en {intentos} intento(s). El número era {numero_secreto}!")
                break
        except ValueError:
            print("Pon un número válido, no letras ni símbolos.")

# Inicio del programa

print("Holaa, soy tu asistente EmaBoss.")
usuario = input("Ingresa tu user compita: ")

while True:
    opcion = input(f"{usuario}, que hacemos..go (calculadora/jugar/adivinar/salir)?: ").lower()
    if opcion == "calculadora":
        calculadora(usuario)
    elif opcion == "jugar":
        piedrapapeltijera(usuario)
    elif opcion == "adivinar":
        adivinar_numero(usuario)
    elif opcion == "salir":
        print("Sayonaraa!")
        break
    else:
        print("tu opcion no es valida xd.")

