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
    print(color(f"\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

# Validaciones de datos
def obtener_datos(dato):
    while True:
        try:
            validacion = input(dato).strip()

            if not validacion:
                raise ValueError(f"\n [-] No se permiten cadenas vacias...")

            return validacion
        except ValueError as e:
            print(e)

# Clases principal
class Tecnologia:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion_vulnerabilidad(self):
        raise NotImplementedError(f"\n[*] Las subclaes definidas deben inplementar este metodo...")

class PcEscritorio(Tecnologia):

    def descripcion_vulnerabilidad(self):
        return color(f"\n[*] Posibles Vulnerabilidades: Sistema operativo windows 7 desactualizado...", "red")

class Laptop(Tecnologia):

    def descripcion_vulnerabilidad(self):
        return color(f"\n[*] Posibles Vulnerabilidades: Backdors en un archivo adjunto pdf", "red")

class TefelofonoCelular(Tecnologia):

    def descripcion_vulnerabilidad(self):
        return color(f"\n[*] Posibles Vulnerabilidades: No se a detectado fallas de seguridad...", "green")

# polimorfismo
def descripcion_vulnerabilidad(Tecnologia):
    print(Tecnologia.descripcion_vulnerabilidad())

# Funcion principal
def main():
    print(color(f"\n[*] Bienvenidos a tecnologiaMexicana", "blue"))

    while True:
        option = input(f"\n[*] Selecciona una opcion:  (1)PcEscritorio  (2)laptop  (3)telefono  (4)limpiarPantalla  (0)terminarPrograma\n\n==>   ")

        if option == "1":
            marca = obtener_datos(f"\n[*] Ingresa la marca:   ")
            modelo = obtener_datos(f"\n[*] Ingresa el modelo:   ")

            pc = PcEscritorio(marca, modelo)
            descripcion_vulnerabilidad(pc)

        elif option == "2":
            marca = obtener_datos(f"\n[*] Ingresa la  marca:   ")
            modelo = obtener_datos(f"\n[*] Ingresa el modelo:   ")

            laptop = Laptop(marca, modelo)
            descripcion_vulnerabilidad(laptop)

        elif option == "3":
            marca = obtener_datos(f"\n[*] Ingresa la marca:   ")
            modelo = obtener_datos(f"\n[*] Ingresa el modelo:   ")

            telefono = TefelofonoCelular(marca, modelo)
            descripcion_vulnerabilidad(telefono)

        elif option == "4":
            
            limpiar_pantalla()

        elif option == "0":

            terminar_programa()

        else:

            print(color(f"\n[-] Error: Intentalo nuevamente...", "red"))


# Flujo principal del programa
if __name__ == "__main__":
    main()
