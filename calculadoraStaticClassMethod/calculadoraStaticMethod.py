#!/usr/bin/env python3

# Librerias
import sys
import signal
import os
from termcolor import colored as color
import time

# Funciones personalizadas

# salir programa
def terminar_programa():
    print(color("[+] Programa terminado correctamente..", "green"))
    sys.exit(0)

# limpiar pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# ctrl_c
def ctrl_c(signal, frame):
    print(color("\n\n[-] Saliendo...", "red"))
    sys.exit(1)
    limpiar_pantalla()

signal.signal(signal.SIGINT, ctrl_c)

# Validar numeros
def validacion_valores(valor):
    while True:
        try:
            valor_validado = float(input(valor))

            if valor_validado < 0:
                print(color("\n[-] Solo se permiten numeros positivos...", "yellow"))
                continue
            elif valor_validado == 0:
                raise ZeroDivisionError(color("\n[-] No se puede dividir entre 0", "yellow"))

            return valor_validado

        except ValueError as e:
            print(color("\n[-] Error invalido, Ingresa un numero valido...", "yellow"))

# Variables globales

# clase calculadora aplicando el metodo staticMethod
class Calculadora:

    # suma
    @staticmethod
    def suma(first_number, second_number):
        resultado = first_number + second_number

        print(color(f"\n[+] La suma de: ( {first_number:.0f} ) + ( {second_number:.0f} ) es ==> {resultado:.0f})", "yellow"))

    # resta
    @staticmethod
    def resta(first_number, second_number):
        resultado = first_number - second_number

        print(color(f"\n[+] La resta de: ( {first_number:.0f} ) - ( {second_number:.0f} ) es ==> {resultado:.0f}", "yellow"))

    # division
    @staticmethod
    def division(first_number, second_number):
        resultado = first_number / second_number

        print(color(f"\n[+] La division de: ( {first_number:.0f} ) / ( {second_number:.0f} ) es ==> {resultado:.1f}", "yellow"))

    # multiplicacion
    @staticmethod
    def multiplicacion(first_number, second_number):
        resultado = first_number * second_number

        print(color(f"\n[+] La multiplicacion de: ( {first_number:.0f} ) * ( {second_number:.0f} ) es ==> {resultado:.0f}", "yellow"))

# Funcion principal
def main():
    print(color("\n[+] Calculadora Basica", "blue"))

    while True:
        option = input("\n[+] Selecciona una opcion:  (1)suma  (2)resta  (3)division  (4)multiplicacion  (5)limpiarPantalla  (0)terminarPrograma\n==>   ")

        if option == "1":
            first_number = validacion_valores("\n[+] Ingresa el primer numero:  ")
            second_number = validacion_valores("\n[+] Ingresa el segundo numero:  ")

            Calculadora.suma(first_number, second_number)
        elif option == "2":
            first_number = validacion_valores("\n[+] Ingresa el primer numero:  ")
            second_number = validacion_valores("\n[+] Ingresa el segundo numero  ")

            Calculadora.resta(first_number, second_number)
        elif option == "3":
            first_number = validacion_valores("\n[+] Ingresa el primer numero:  ")
            second_number = validacion_valores("\n[+] Ingresa el segundo numero:  ")

            Calculadora.division(first_number, second_number)
        elif option == "4":
            first_number = validacion_valores("\n[+] Ingresa el primer numero:  ")
            second_number = validacion_valores("\n[+] Ingresa el segundo numero:  ")

            Calculadora.multiplicacion(first_number, second_number)
        elif option == "5":
            limpiar_pantalla()
        elif option == "0":
            terminar_programa()
        else:
            print(color("\n[-] Opcion invalida...", "yellow"))

# Flujo principal del programa
if __name__ == "__main__":
    main()
