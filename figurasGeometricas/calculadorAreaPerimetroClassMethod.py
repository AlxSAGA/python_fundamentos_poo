

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
    limpiar_pantalla()
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
    def __init__(self, ancho, largo=0):
        self.ancho = ancho 
        self.largo = largo

    """
    - Área = π × radio²             (A = π * r²)
    - Perímetro (circunferencia) = 2 × π × radio  (P = 2πr)
    """
    @property
    def calcular_circulo(self):
        PI = 3.1416
        radio = self.ancho

        area = PI * (radio ** 2)
        perimetro = 2 * PI * radio

        print(color(f"\n[+] El area es: ( {area:.2f} cm)", "blue"))
        print(color(f"[+] El perimetro es: ( {perimetro:.2f} )", "blue"))

    """
    - Área = lado²                  (A = l²)
    - Perímetro = 4 × lado          (P = 4l)
    """
    @property
    def calcular_cuadrado(self):
        lado = self.ancho

        area = lado ** 2
        perimetro = 4 * lado

        print(color(f"\n[+] El area es: ( {area:.0f} cm)","blue"))
        print(color(f"\n[+] El perimetro es: ( {perimetro:.0f} )", "blue"))

    """
    - Área = ancho × largo           (A = a × l)
    - Perímetro = 2 × (ancho + largo)  (P = 2(a + l))
    """
    @property 
    def calcular_rectangulo(self):
        area = self.ancho * self.largo
        perimetro = 2 * (self.ancho + self.largo)

        print(color(f"\n[+] El area es: ( {area:.0f} cm)","blue"))
        print(color(f"\n[+] El perimetro es: ( {perimetro:.0f} cm)","blue"))

    """
    TRIÁNGULO (EQUILÁTERO):
    - Área = (base × altura)/2       (A = (b × h)/2)
    - Perímetro = 3 × lado           (P = 3l)
    """
    @property
    def calcular_triangulo(self):
        area = (self.ancho * self.largo) / 2
        perimetro = 3 * self.ancho

        print(color(f"[+] El area es: ( {area:.0f} cm)", "blue"))
        print(color(f"[+] El perimetro es: ( {perimetro:.0f} cm)","blue"))

# Funcion principal
def main():
    print(color("\n\n[+] Bienvenido al programa de calculo de area y perimetro de figuras geometricas.\n", "blue"))

    while True:
        option = input("\n[+] Selecciona una figura geometrica: (1)Circulo, (2)Cuadrado, (3)Rectangulo, (4)Triangulo, (5)Limpiar Pantalla, (0)Terminar Programa\n==>  ")

        if option == "1":
            radio = obtener_numero_positivo("\n[+] Radio del circulo?  ")

            circulo = CalculoFigurasGeometricas(radio)
            circulo.calcular_circulo
        elif option == "2":
            lado = obtener_numero_positivo("\n[+] Longitud del lado?  ")

            cuadrado = CalculoFigurasGeometricas(lado)
            cuadrado.calcular_cuadrado
        elif option == "3":
            largo_figura = obtener_numero_positivo("\n[+] Largo del rectangulo?  ")
            ancho_figura = obtener_numero_positivo("[+] Ancho del rectangulo?  ")

            rectangulo = CalculoFigurasGeometricas(largo_figura, ancho_figura)
            rectangulo.calcular_rectangulo
        elif option == "4":
            base = obtener_numero_positivo("\n[+] Ancho de la base?  ")
            altura = obtener_numero_positivo("\n[+] Altura del triangulo?  ")

            triangulo = CalculoFigurasGeometricas(base, altura)
            triangulo.calcular_triangulo
        elif option == "5":
            limpiar_pantalla()
            
        elif option == "0":
            salir()
            
        else:
            print(color("\n[-] Opción no válida. Por favor selecciona una opción del 1 al 6.", "red"))

# Flujo principal del programa
if __name__ == "__main__":
    main()
