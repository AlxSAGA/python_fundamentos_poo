#!/usr/bin/env python3

# Libvrerias
import sys
from termcolor import colored as c
import signal
import os 

# Funciones personalizadas
def ctrl_c(signum, frame):
    print(c("\n\n[-] Saliendo ...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def salir():
    print(c("\n\n[-] Programa terminado", "red"))
    exit(0)

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Seccion Banco
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo # Atributo privado

    def __str__(self):
        return f"{self.__saldo}"

    # Seccioon Saldo Cliente
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(c(f"\nDeposito exitoso. Nuevo saldo: {self.__saldo}", "green"))
        else:
            print(c(f"\n[-] Deposito fallido(la Cantidad {cantidad} No es valida)...", "red"))

    # Seccion Retiro Cliente
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            
            print(c(f"\nRetiro exitoso. Nuevo saldo: {self.__saldo}", "green"))
        else:
            print(c("\n[-] Retiro fallido. Fondos insuficientes...", "red"))

    # Seccion Consulta Saldo Cliente
    def consultar_saldo(self):
        return c(f"\nCliente: {self.titular}, Saldo: {self.__saldo}", "magenta")

# Seccion clientes
alex = CuentaBancaria("Alex Salazar", 1000)


# Seccion principal clientes
def main():
    print(c(f"\n[+] Bienvenido a BancoMexicano: ( {alex.titular} )\n\t[ * ]Saldo Disponible: {alex}", "cyan"))

    while True:
        option = input(c("\n[+] Selecciona una opcion: (1)Despositar (2)Retirar (3)Consultar Saldo (4)Limpiar Pantalla (0)Terminar Programa:  ", "yellow"))

        if option == "1":
            alex.depositar(float(input(c("\n[+] Depositar:  ", "green"))))
        elif option =="2":
            alex.retirar(float(input(c("\n[-] Retirar:  ", 'green'))))
        elif option == "3":
            print(alex.consultar_saldo())
        elif option == "4":
            limpiar_pantalla()
        elif option == "0":
            salir()
        else:
            print(c("\n[-] Opcion no valida", "red"))
# Flujo principal:
if __name__ == "__main__":
        main()
