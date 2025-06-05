#!/usr/bin/env python3

# Librerias
import sys, signal, os 
from termcolor import colored as color 

# Funciones personalizads
def ctrl_c(signal, frame):
    print(color(f"\n[-] Saliendo...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def terminar_programa():
    print(color(f"\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Validacion datos
def obtener_datos(dato):
    while True:
        try:
        
            validacion = input(dato).strip()

            if not validacion:
                raise ValueError("[-] No se permiten cadenas vacias...")
                
            return validacion

        except ValueError as e:
            print(e)

# Clase principal
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return color(f"\n[+] Autor: ( {self.autor} ) - Titulo: ( {self.titulo} )", "cyan")

    # Comprobacion libros iguales
    def __eq__(self, otro):
        return self.autor == otro.autor and self.titulo == otro.titulo
            

# Funcion principal 
def main():
    print(color("\n[+] Bienvenidos a tienda libroMexicano", "blue"))

    while True:
        option = input("\n[+] Selecciona una opcion:  (1)registrarLibro - (2)limpiar_pantalla - (0)terminarPrograma\n\n==>   ")

        if option == "1":
            
            titulo_libro = obtener_datos("\n[+] Ingresa el titulo:   ")
            autor_libro = obtener_datos("\n[+] Ingresa el nombre del autor:  ")

            libro_uno= Libro(titulo_libro, autor_libro)
            print(libro_uno)

            #print(color(f"[+] Son iguales?  ( {libro_uno == libro_uno} )"))

        elif option == "2":

            limpiar_pantalla()

        elif option == "0":

            terminar_programa()

        else:

            print(color(f"\n[-] Error: Intentalo nuevamente...", "red"))
    
# Flujo principal del programa
if __name__ == "__main__":
    main()
