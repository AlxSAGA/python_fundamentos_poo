#!/usr/bin/env python3

# Librerias
import sys
import signal
import os
import time 
from termcolor import colored as color 

# Funciones personalizadas

# funcion terminar programa forzado
def ctrl_c(signal, frame):
    print(color("\n\n[-] Saliendo...", "red"))
    sys.exit(1)
    limpiar_pantalla()

signal.signal(signal.SIGINT, ctrl_c)

# funcion limpiar pantalla 
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# funcion terminar programa 
def terminar_programa():
    print(color("\n\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)
    limpiar_pantalla()

# Validaciones datos
def obtener_dato(dato):
    while True:
        try:
            entrada = input(dato).strip()
            if not entrada:
                raise ValueError("[-] Error: No puedes ingresar una cadena vacía")
            for caracter in entrada:
                if not caracter.isalpha() and caracter != ' ':
                    raise ValueError("[-] Error: Solo se permiten letras y espacios")
            return entrada
        except ValueError as e:
            print(color(f"\n{str(e)}. Intenta nuevamente.", "red"))
            
# Clase principal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        raise NotImplementedError("\n[+] Las subclases definidas deben implementar este metodo...")

class Perro(Animal):
    def sonido(self):
        print(color(f"\n[+] ( {self.nombre} ) dice: guaw guaw", "blue"))

class Gato(Animal):
    def sonido(self):
        print(color(f"\n[+] ( {self.nombre} ) dice: miau miau", "blue"))

class Perico(Animal):
    def sonido(self):
        print(color(f"\n[+] ( {self.nombre} ) dice: rocky cotoroky", "blue"))

# Funcion principal
def main():
    print(color("\n[+] Bienvenidos a tienda mascotaMexicana...", "blue"))

    while True:
        option = input("\n[+] Selecciona una opcion:  (1)Perro  (2)Gato  (3)Perico  (4)limpiarPantalla  (0)terminarPrograma\n==>  ")

        if option == "1":
            nombre_perro = obtener_dato("\n[+] Ingresa el nombre de tu mascota:  ")

            perro = Perro(nombre_perro)
            perro.sonido()
        elif option == "2":
            nombre_gato = obtener_dato("\n[+] Ingresa el nombre de tu mascota:  ")

            gato = Gato(nombre_gato)
            gato.sonido()
        elif option == "3":
            nombre_perico = obtener_dato("\n[+] Ingresa el nombre de tu mascota:  ")

            perico = Perico(nombre_perico)
            perico.sonido()
        elif option == "4":
            limpiar_pantalla()
        elif option == "0":
            terminar_programa()
        else:
            print(color("\n\n[-] Erro: opcion invalida...", "yellow"))

# Flujo del program
if __name__ == "__main__":
    main()
