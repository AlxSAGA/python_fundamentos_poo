#!/usr/bin/env python3

# Librerias ===================================================================================================================
import sys
import signal
import os
from termcolor import colored as color

# Funciones personalizadas =====================================================================================================

# funcion terminar programa forzado
def ctrl_c(signal, frame):
    print(color("\n\n[-] Saliendo....", "red"))
    sys.exit(1)
    limpiar_pantalla()

signal.signal(signal.SIGINT, ctrl_c)

# funcion limpiar limpiar_pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# funcion terminar programa
def terminar_programa():
    print(color("\n[+] Programa termiando correctamente...", "green"))
    sys.exit(0)

# funcion para validar los datos ===================================================================================================
def obtener_nombre(nombre_estudiante):
    while True:
        try:
            entrada = input(nombre_estudiante).strip()
            if not entrada:
                raise ValueError("[-] Error: No puedes ingresar una cadena vacía")
            for caracter in entrada:
                if not caracter.isalpha() and caracter != ' ':
                    raise ValueError("[-] Error: Solo se permiten letras y espacios")
            return entrada
        except ValueError as e:
            print(color(f"\n{str(e)}. Intenta nuevamente.", "red"))

def obtener_edad(edad_estudiante):
    while True:
        try:
            entrada = input(edad_estudiante).strip()
            if not entrada:
                raise ValueError("[-] Error: No puedes ingresar una cadena vacía")
            edad = int(entrada)
            if edad < 0:
                raise ValueError("[-] Error: La edad no puede ser negativa")
            if edad > 30:
                raise ValueError("[-] Error: La edad no puede ser mayor a 30 años")
            return edad
        except ValueError as e:
            print(color(f"\n{str(e)}. Intenta nuevamente.", "red"))


# Clase principal =========================================================================================================================
class Escuela:
    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        Escuela.estudiantes.append(self)
        print(color("\n[+] Estudiante creado correctamente...", "cyan"))

    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18

    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.es_mayor_edad(edad):
            return cls(nombre, edad)
        else:
            print(color(f"\n\n[-] Error: El estudiante ( {nombre} ) es menor de edad...", "red"))

    @staticmethod
    def mostrar_estudiantes():
        print(color("\n[+] Estudiantes activos en escuelaMexicana...", "cyan"))
        for i, estudiante in enumerate(Escuela.estudiantes):
            print(color(f"\n( {i+1} ) {estudiante.nombre.title()}", "cyan"))

# Funcion principal
def main():
    print(color("\n[+] Bienvenidos a escuelaMexicana", "red"))

    while True:
        option = input("\n[+] Selecciona una opcion:  (1)registrarEstudiante  (2)mostrarEstudiantes  (3)limpiarPantalla  (0)terminarPrograma\n==>   ")

        if option == "1":
            nombre_estudiante = obtener_nombre("\n[+] Ingresar nombre completo del estudiante:   ")
            edad_estudiante = obtener_edad("\n[+] Ingresar edad del estudiante:  ")

            Escuela.crear_estudiante(nombre_estudiante, edad_estudiante)
        elif option == "2":
            Escuela.mostrar_estudiantes()
        elif option == "3":
            limpiar_pantalla()
        elif option == "0":
            terminar_programa()
        else:
            print(color("\n[-] Erro: Opcion invalida..", "yellow"))

# Flujo principal del programa
if __name__ == "__main__":
    main()
