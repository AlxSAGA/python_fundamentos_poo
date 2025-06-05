#!/usr/bin/env python3

# Librerias
import sys, signal, os
from termcolor import colored as color

# Funciones Personalizadas
def ctrl_c(signal, frame):
    print(color(f"\n\n[+] Saliendo...", "red"))
    sys.exit(1)

# ctrl_c
signal.signal(signal.SIGINT, ctrl_c)

def terminar_programa():
    print(color(f"\n\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Classe principal
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property 
    def mostar_edad(self): # Getter
        return self._edad

    @mostar_edad.setter # setter
    def mostar_edad(self, valor):
        while True:
            try:
                if valor > 0:
                    self._edad = valor

                else:

                    raise ValueError("[-] La edad no puede ser un numero negativo...")

            except ValueError as e:
                print(e)

# Funcion principal
def main():
    print(color(f"\n[+] Bienvenidos...."))

    while True:
        option = input(f"\n[+] Selecciona una opcion:  (1)registrarPersona - (2)limpiarPantalla - (0)terminarPrograma\n\n==>  ")

        if option == "1":

            nombre_persona = input(f"\n[+] Cual es el nombre?  ")
            edad_persona = int(input(f"\n[+] Cual es la edad  "))

            persona = Persona(nombre_persona, edad_persona)
            print(persona)

        elif option == "2":

            limpiar_pantalla()

        elif option == "0":
            
            terminar_programa()

        else:
            
            print(color(f"\n[-] Error: Vuelve a intentarlo...", "red"))

# Flujo principal del programa
if __name__ == "__main__":
    main()

