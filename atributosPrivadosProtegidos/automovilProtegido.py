#!/usr/bin/env python3

# Librerias
import sys, signal, os
from termcolor import colored as color 

# Funciones personalizadas
def ctrl_c(signal, frame):
    print(color(f"\n\n[-] Saliendo...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def terminar_programa():
    print(color(f"\n[+] Programa finalizado correctamente...", "green"))
    sys.exit(0)

# Validacion de datos
def obtener_dato(data):
    while True:
        try:
            validacion = input(data).strip()

            if not validacion:
                raise ValueError(f"\n[-] No se permiten cadenas vacias...")

            validacion_numero = int(validacion)

            if validacion_numero <= 0:
                raise ValueError(f"\n[-] No se permiten numeros negativos...")

            return validacion_numero
        except ValueError as e:
            print(e)

# Clase principal
class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0

    def hacelerar(self, kilometraje_hacelerado):
        
        if kilometraje_hacelerado > 0:
            self.__kilometraje += kilometraje_hacelerado

    def mostrar_kilometraje(self):
        return color(f"\n( {self.marca} )( {self.modelo} ) Kilometraje Actualizado: ( {self.__kilometraje} )") 

# Funcion principal
def main():
    print(color(f"\n[+] Bienvenido.. a automotrizMexicana", "blue"))

    while True:
        option = input("\n[+] Selecciona una opcion del menu: (1)Hacelerar Automovil - (2)Limpiar Pantalla - (0)Terminar Programa: ==>   ")

        if option == "1":

            marca = input("\n[+] Ingresa la marca del automovil:  ")
            modelo = input("\n[+] Ingresa el modelo del automovil:  ")

            hacelerar_automovil = obtener_dato(f"\n[+] Ingresa un numero:   ")

            automovil = Automovil(marca, modelo)
            automovil.hacelerar(hacelerar_automovil)
            print(automovil.mostrar_kilometraje())

        elif option == "2":

            limpiar_pantalla()

        elif option == "0":

            terminar_programa()

        else:

            print(color(f"[+] Error: Opcion invalida..", "red"))


# Flujo principal del programa
if __name__ == "__main__":
    main()
