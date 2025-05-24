import tkinter as tk
from tkinter import simpledialog, messagebox
import random

operaciones = ["+", "-", "*", "/"]

class EmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EmaBoss App")
        self.nombre = ""

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        self.bienvenida()

    def bienvenida(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Bienvenido a EmaBoss", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Ingresar nombre", command=self.pedir_nombre).pack(pady=5)

    def pedir_nombre(self):
        self.nombre = simpledialog.askstring("Nombre", "Ingresa tu user compita:")
        if self.nombre:
            self.menu_principal()

    def menu_principal(self):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"Hola {self.nombre}, ¿qué hacemos?", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.main_frame, text="Calculadora", width=20, command=self.calculadora).pack(pady=5)
        tk.Button(self.main_frame, text="Piedra, Papel o Tijera", width=20, command=self.piedrapapeltijera).pack(pady=5)
        tk.Button(self.main_frame, text="Adivinar Número", width=20, command=self.adivinar_numero).pack(pady=5)
        tk.Button(self.main_frame, text="Salir", width=20, command=self.root.quit).pack(pady=5)

    def calculadora(self):
        try:
            num1 = int(simpledialog.askstring("Calculadora", f"{self.nombre}, inserta número 1:"))
            num2 = int(simpledialog.askstring("Calculadora", "Inserta número 2:"))
            operacion = simpledialog.askstring("Calculadora", "Selecciona operación [+ - * /]:")

            if operacion not in operaciones:
                messagebox.showerror("Error", "Operación inválida")
                return

            if operacion == "/" and num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre 0")
            else:
                resultado = eval(f"{num1} {operacion} {num2}")
                messagebox.showinfo("Resultado", f"{num1} {operacion} {num2} = {resultado}")
        except:
            messagebox.showerror("Error", "Entrada inválida")

    def piedrapapeltijera(self):
        opciones = ["piedra", "papel", "tijera"]
        jugador = simpledialog.askstring("Juego", f"{self.nombre}, elige: piedra, papel o tijera:").lower()
        if jugador not in opciones:
            messagebox.showwarning("Ups", "Opción inválida")
            return
        maquina = random.choice(opciones)
        resultado = f"EmaBoss eligió: {maquina}\n"
        if jugador == maquina:
            resultado += "DIOS! es un Empate"
        elif (jugador == "piedra" and maquina == "tijera") or \
             (jugador == "papel" and maquina == "piedra") or \
             (jugador == "tijera" and maquina == "papel"):
            resultado += "¡Ganaste mi rey!"
        else:
            resultado += "Suerte a la próxima, panita."
        messagebox.showinfo("Resultado", resultado)

    def adivinar_numero(self):
        numero_secreto = random.randint(1, 10)
        intentos = 0
        while True:
            try:
                intento = int(simpledialog.askstring("Adivina", f"{self.nombre}, adivina un número del 1 al 10:"))
                intentos += 1
                if intento < 1 or intento > 10:
                    messagebox.showinfo("Pista", "Debe ser entre 1 y 10")
                elif intento < numero_secreto:
                    messagebox.showinfo("Pista", "Muy bajito")
                elif intento > numero_secreto:
                    messagebox.showinfo("Pista", "Te pasaste xd")
                else:
                    messagebox.showinfo("Ganaste", f"Lo lograste en {intentos} intento(s)! Era el {numero_secreto}")
                    break
            except:
                messagebox.showerror("Error", "Entrada inválida")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmaApp(root)
    root.mainloop()