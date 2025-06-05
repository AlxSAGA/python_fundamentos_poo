
#!/usr/bin/env pythonu3

# Librerias
import sys
import signal
import os
from termcolor import colored as color

# Funciones Personalizadas
def salir_programa():
    print(color("\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def ctrl_c(signal, frame):
    print(color("\n[-] Saliendo ...", "red"))
    sys.exit(1)
    limpiar_pantalla()

signal.signal(signal.SIGINT, ctrl_c)

# clase principal
class Libro:
    
    IVA = 0.21
    bestseller_value = 500

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def agregar_libro(self):
        print(color(f"\n[+] Libro registrado exitosamente..", "blue"))

    # Para libros con mejores ventas:
    @staticmethod
    def es_bestseller(total_ventas):
        if total_ventas > Libro.bestseller_value:
            print(color(f"\n[+] Libro con caterotia: ( Bestseller )","blue"))

    # Calculamos el iva.
    @classmethod
    def precio_iva(cls, precio):
        precio_iva = precio + precio * cls.IVA 

        print(color(f"[+] El precion con iba es: [{precio_iva:.2f}]"))

# Funcion principal
def main():
    print(color("\n\n[+] Bienvenido a biblioteca mexicana...", "blue"))
    
    while True:
        option = input("\nMenu: (1)registrarLibro  (2)limpiarPantall  (0)terminarPrograma\n==>  ")

        if option == "1":
            titulo_libro = input("\n[+] Titulo del libro?  ")
            autor_libro = input("[+] Autor del libro?  ")
            precio_libro = float(input("[+] Precio del libro?  "))
            ventas_libro = int(input("\n[+] Ventas totales?  "))

            libro = Libro(titulo_libro, autor_libro, precio_libro)
            libro.agregar_libro()

            Libro.es_bestseller(ventas_libro)
            Libro.precio_iva(libro.precio)

        elif option == "2":
            limpiar_pantalla()
        elif option == "0":
            salir_programa()
        else:
            print(color("\n[-] Opcion incorecta...", "red"))

# Flujo principal
if __name__ == "__main__":
    main()
