#!/usr/bin/env python3

# Librerias
import sys, signal, os
from termcolor import colored as color 

# funciones personalizadas 
def ctrl_c(signal, frame):
    print(color(f"\n\n[*] Saliendo...", "red"))
    sys.exit(1)
    limpiar_pantalla()

signal.signal(signal.SIGINT, ctrl_c)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def terminar_programa():
    print(color(f"\n[*] Programa termiando correctamente...", "green"))
    sys.exit(0)

# Validacion datos
def obtener_dato(dato):
    while True:
        try:
            validacion = input(dato).strip()
            if not validacion:
                raise ValueError(f"\n[-] No se permiten cadenas vacias")
            
            return validacion
        except ValueError:
            print(color(f"[-] Intentalo nuevamente...", "red"))

# clase principal
class TecnologiaRuedas:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        raise NotImplementedError("\n[*] Las subclases definidas deben implementar este metodo...")

class Automovil(TecnologiaRuedas):
    def describir(self):
        return color(f"\n[*] Automovil: ( {self.marca} ) ( {self.modelo} )", "yellow")

class Motocicleta(TecnologiaRuedas):
    def describir(self):
        return color(f"\n[*] Motocicleta: ( {self.marca} ) ( {self.modelo} )", "yellow")

# Polimorfismo
def describir(TecnologiaRuedas):
    print(TecnologiaRuedas.describir())

# funcion principal
def main():
    print(color(f"\n[*] Bienvenidos a TecnologiaRuedasMexicana", "blue"))

    while True:
        option = input(color(f"\n[*] Sececciona una opcion:  (1)registrarAutomovil  (2)registrarMotocicleta  (3)limpiarPantalla  (0)terminarPrograma\n\n==>   "))

        if option == "1":
            marca = obtener_dato(f"\n[*] Ingresa la marca:   ")
            modelo = obtener_dato(f"\n[*] Ingresa el modelo   ")

            automovil = Automovil(marca, modelo)
            describir(automovil)

        elif option == "2":
            marca = obtener_dato(f"\n[+] Ingresa la marca:   ")
            modelo = obtener_dato(f"[*] Ingresa el modelo:   ")

            motocicleta = Motocicleta(marca, modelo)
            describir(motocicleta)

        elif option == "3":
            limpiar_pantalla()

        elif option == "0":

            terminar_programa()

        else:

            print(color(f"\n[*] Error, Opcion invalida...", "red"))

# flujo principal del programa 
if __name__ == "__main__":
    main()
