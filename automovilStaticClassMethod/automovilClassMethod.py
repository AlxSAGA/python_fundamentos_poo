#!/usr/bin/env python3

# Librerias
import sys
import signal
import os
from termcolor import colored as color

# Variables globlales

# Funciones personalizadas

# terminara programa forzado
def ctrl_c(signal, frame):
    print(color("\n\n[-] Saliendo...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

# limpiar limpiar pantall
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# terminar programa
def terminar_programa():
    print(color("\n\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

# validacion de datos
def obtener_texto(dato):
    while True:
        try:
            entrada = input(dato).strip()
            
            if not entrada:
                raise ValueError("[-] Error: No puedes ingresar una cadena vacía")
            
            # Validar caracteres permitidos
            for caracter in entrada:
                if not caracter.isalpha() and caracter != ' ':
                    raise ValueError("[-] Error: Solo se permiten letras y espacios")
            
            return entrada
        
        except ValueError as e:
            print(color(f"\n{str(e)}. Intenta nuevamente.", "red"))

# clases del programa
class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def deportivo(cls, marca):
        return cls(marca, "Deportivo")

    def __str__(self):
        return color(f"\n[+] ( {self.marca} ) -  Modelo: ( {self.modelo} )")

# Funcion principal
def main():
    print(color("\n[+] Bienvenidos a mexicanaAutomotriz", "magenta"))

    while True:
        option = input("\n[+] Selecciona una opcion:  (1)verAutomovil  (2)limpiar_pantalla  (0)terminarPrograma\n==>  ")

        if option == "1":
            marca_automovil = obtener_texto("\n[=] Ingresa la maraca del automovil:  ")
            auto = Automovil.deportivo(marca_automovil)
            print(auto)
        elif option == "2":
            limpiar_pantalla()
        elif option == "0":
            terminar_programa()
        else:
            print(color("\n\n[-] Opcion invalida...", "yellow"))


# Flujo principal 
if __name__ == "__main__":
    main()
