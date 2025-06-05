#!/usr/bin/env python3

# Librerias
import sys
import signal
import os
from termcolor import colored as color

# Funciones personalizadas
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def salir():
    print(color("\n\n[+] Programa terminado exitosamente.\n", "green"))
    sys.exit(0)

def ctrl_c(signal, frame):
    print(color("\n\n[-] Saliendo del programa...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

# Función para validar números positivos
def obtener_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print(color("\n[-] Error: El valor debe ser positivo. Intenta nuevamente.", "red"))
                continue
            return valor
        except ValueError:
            print(color("\n[-] Error: Debes ingresar un número válido. Intenta nuevamente.", "red"))

# Funciones de calculo
class CalculoFigurasGeometricas:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

    def calcular_circulo(self, radio):
        PI = 3.1416
        resultado_area = PI * (radio ** 2)
        resultado_perimetro = 2 * PI * radio

        print(color(f"\n[+] El area del circulo es: ( {resultado_area:.2f} cm )", "green"))
        print(color(f"[+] El perimetro del circulo es: ( {resultado_perimetro:.2f} cm )", "green"))

    def calcular_cuadrado(self, lado_cuadrado):
        resultado_area = (lado_cuadrado ** 2)
        resultado_perimetro = (4 * lado_cuadrado)

        print(color(f"\n[+] El area del cuadrado es: ( {resultado_area:.0f} cm )", "green"))
        print(color(f"[+] El perimetro del cuadrado es: ( {resultado_perimetro:.0f} cm )", "green"))

    def calcular_rectangulo(self, largo_rectangulo, ancho_rectangulo):
        resultado_area = (largo_rectangulo * ancho_rectangulo)
        resultado_perimetro = (2 * (largo_rectangulo + ancho_rectangulo))

        print(color(f"\n[+] El area del rectangulo es: ( {resultado_area:.0f} cm)", "green"))
        print(color(f"[+] El perimetro del rectangulo es: ( {resultado_perimetro:.0f} cm)", "green"))

    def calcular_triangulo(self, base_triangulo, altura_triangulo):
        resultado_area = (base_triangulo * altura_triangulo) / 2
        resultado_perimetro = (base_triangulo * 3)

        print(color(f"\n[+] El area del triangulo es: ( {resultado_area:.0f} cm)", "green"))
        print(color(f"[+] El perimetro del triangulo es: ({resultado_perimetro:.0f} cm )", "green"))
    
# Seccion figuras geometricas
figura = CalculoFigurasGeometricas()

# Funcion principal
def main():
    print(color("\n\n[+] Bienvenido al programa de calculo de area y perimetro de figuras geometricas.\n", "blue"))

    while True:
        option = input("\n[+] Selecciona una figura geometrica: (1)Circulo, (2)Cuadrado, (3)Rectangulo, (4)Triangulo, (5)Limpiar Pantalla, (6)Terminar Programa\n==>  ")

        if option == "1":
            print("\n[+] Has seleccionado el círculo")
            radio = obtener_numero_positivo("[+] Ingresa el radio (cm): ")
            figura.calcular_circulo(radio)
            
        elif option == "2":
            print("\n[+] Has seleccionado el cuadrado")
            lado = obtener_numero_positivo("[+] Ingresa el lado del cuadrado (cm): ")
            figura.calcular_cuadrado(lado)
            
        elif option == "3":
            print("\n[+] Has seleccionado el rectángulo")
            largo = obtener_numero_positivo("[+] Ingresa el largo (cm): ")
            ancho = obtener_numero_positivo("[+] Ingresa el ancho (cm): ")
            figura.calcular_rectangulo(largo, ancho)
            
        elif option == "4":
            print("\n[+] Has seleccionado el triángulo")
            base = obtener_numero_positivo("[+] Ingresa la base (cm): ")
            altura = obtener_numero_positivo("[+] Ingresa la altura (cm): ")
            figura.calcular_triangulo(base, altura)
            
        elif option == "5":
            limpiar_pantalla()
            
        elif option == "0":
            salir()
            
        else:
            print(color("\n[-] Opción no válida. Por favor selecciona una opción del 1 al 6.", "red"))

# Flujo principal del programa
if __name__ == "__main__":
    main()
