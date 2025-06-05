#!/usr/bin/env python3

# Librerias
import sys, signal, os 
from termcolor import colored as color 

# Funciones personalizadas
def ctrl_c(signal, frame):
    print(color(f"\n[-] Saliendo...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def terminar_programa():
    print(color(f"\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Validacion de datos
def obtener_datos(data):
    while True:
        
        try:
            validacion_item = input(data).strip()

            if not validacion_item:
                raise ValueError("\n[-] No se permiten cadenas vacias...")

            for character in validacion_item:
                if not character.isalpha() and character != ' ':
                    raise ValueError("\n[-] Solo se permiten letras...")

            return validacion_item

        except ValueError as e:
            print(e)

# Clase principal
class CentralAbasto:
    
    def __init__(self, *items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Funcion principal
def main():
    print(color("\n[+] Bienvenidos a centralAbastoMexicana", "blue"))

    while True:
        option = input("\n[+] Selecciona una opcion del menu:  (1)registrarFruta - (2)limpiarPantalla - (0)terminarPrograma\n\n==>   ")

        if option == "1":
            
            option_item = obtener_datos("\n[+] Ingresa la fruta o frutas?   ")

            item = CentralAbasto(option_item)
            print(len(item))

        elif option == "2":

            limpiar_pantalla()

        elif option == "0":

            terminar_programa()

        else:

            print(color(f"\nError: Opcion invalida...", "red"))


# Flujo pripal del programa
if __name__ == "__main__":
    main()
