#!/usr/bin/env python3

# Librerias
from termcolor import colored as c
import signal
import sys

# Datos tiendaGamer
juegos_generos = {
    "Fortnite": "Battle Royale",
    "Call of Duty: Modern Warfare II": "FPS",
    "FC 25": "Deportes",
    "Warzone": "Battle Royale",
    "The Legend of Zelda: Tears of the Kingdom": "Acción-Aventura",
    "Minecraft": "Sandbox",
    "Grand Theft Auto V": "Acción-Aventura",
    "Apex Legends": "Battle Royale",
    "League of Legends": "MOBA",
    "Valorant": "FPS Táctico",
    "Overwatch 2": "FPS por Equipos",
    "PUBG: Battlegrounds": "Battle Royale",
    "Elden Ring": "RPG de Acción",
    "Rocket League": "Deportes Vehicular",
    "Counter-Strike 2": "FPS Táctico",
    "Among Us": "Party/Social Deducción",
    "Super Mario Odyssey": "Plataformas 3D",
    "Animal Crossing: New Horizons": "Simulación",
    "God of War: Ragnarök": "Acción-Aventura",
    "Red Dead Redemption 2": "Acción-Aventura"
}

# Ventas y Clientes
ventas_stock = {
    "Fortnite": (350, 45),
    "Call of Duty: Modern Warfare II": (28, 15),
    "FC 25": (12, 8),
    "Warzone": (90, 25),
    "The Legend of Zelda: Tears of the Kingdom": (25, 3),
    "Minecraft": (300, 50),
    "Grand Theft Auto V": (185, 20),
    "Apex Legends": (70, 18),
    "League of Legends": (150, 0),  # Free-to-play
    "Valorant": (50, 12),
    "Overwatch 2": (25, 10),
    "PUBG: Battlegrounds": (75, 20),
    "Elden Ring": (20, 5),
    "Rocket League": (15, 6),
    "Counter-Strike 2": (35, 8),
    "Among Us": (60, 15),
    "Super Mario Odyssey": (27, 4),
    "Animal Crossing: New Horizons": (40, 8),
    "God of War: Ragnarök": (18, 3),
    "Red Dead Redemption 2": (55, 10)
}
# Clientes
clientes = {
    "Fortnite": {"Carlos", "Ana", "Pedro", "Sofía"},
    "Call of Duty: Modern Warfare II": {"Luis", "Diego", "Marta", "Raúl"},
    "FC 25": {"Juan", "Lucía", "Andrés", "Carmen"},
    "Warzone": {"Laura", "Javier", "Elena"},
    "The Legend of Zelda: Tears of the Kingdom": {"David", "Sara", "Miguel", "Paula"},
    "Minecraft": {"Alberto", "Clara", "Daniel", "Olivia"},
    "Grand Theft Auto V": {"Roberto", "Marina", "Héctor"},
    "Apex Legends": {"Natalia", "Alejandro", "Beatriz", "Guillermo"},
    "League of Legends": {"Adrián", "Celia", "Rubén", "Lorena"},
    "Valorant": {"Víctor", "Silvia", "Iván"},
    "Overwatch 2": {"Mario", "Rocío", "Fernando", "Alicia"},
    "PUBG: Battlegrounds": {"Óscar", "Nerea", "Pablo"},
    "Elden Ring": {"Jorge", "Eva", "Martín", "Patricia"},
    "Rocket League": {"Ángel", "Teresa", "Gabriel", "Raquel"},
    "Counter-Strike 2": {"Simón", "Cristina", "Marcos"},
    "Among Us": {"Lucas", "María", "Julia", "Hugo"},
    "Super Mario Odyssey": {"Iker", "Valeria", "Manuel"},
    "Animal Crossing: New Horizons": {"Nora", "Alba", "Gonzalo", "Carla"},
    "God of War: Ragnarök": {"Borja", "Diana", "Samuel"},
    "Red Dead Redemption 2": {"Jaime", "Andrea", "Francisco", "Miriam"}
}

# Funciones programa:
def ctrl_c(signum, frame):
    print(c("\n\n[-] Saliendo ...", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def terminar_programa():
    print(c("\n[-] Programa terminado...", 'red'))
    exit()

# Funciones tiendaGamer
def listar_juegos():
    juegos = ' - '.join([juego for juego in juegos_generos.keys()])
    print(f"\n[+] Juegos disponibles en tiendaGamer\n{c(juegos, 'green')}")

    menu = c("\n[+] ( 1 )Ver detalles ( 0 )Menu principal ==> ", 'blue')
    option_menu = str(input(menu))
    
    if option_menu == "1":
        option_nombre = str(input("\n[+] Ingresa el nombre del juego: ==> "))

        if option_nombre in juegos:
            print(f"\n[+] Nombre: {option_nombre}")
            print(f"\tGenero: {juegos_generos[option_nombre]}")
        else:
            print(c("\n[-] Juego no encontrado...", 'red'))

    elif option_menu == "0":
       main()
    else:
        print(c("\n[-] Opcion no valida, Elige una opcion correcta...", 'red'))

def listar_ventas():
    for juego, venta_stock in ventas_stock.items():
        print(c(f"[+] ( {juego} ) ==> Ventas: {venta_stock[0]} unidades - Stock: {venta_stock[1]} unidades", 'cyan'))

def listar_clientes():
    for juego, cliente in clientes.items():
        print(c(f"[+] ( {juego} ) ==> Clientes: {', '.join(cliente)}", 'cyan'))

def top_ventas():
    print(c("\n[+] Top ventas juegos en tiendaGamer", 'green'))

    for juego, ventas_top in ventas_stock.items():
        if ventas_top[0] >= 60:
            print(c(f"\t[+] ( {juego} ) ==> Ventas: {ventas_top[0]} Unidades", 'cyan'))

# Funcion lambda ventas totales
ventas_totales = lambda: sum(ventas for ventas, _ in ventas_stock.values())

# Principal 
def main():
    while True:
        print(c(f"\nBienvenido a tiendaGamer\n", 'blue'))

        menu = c("( 1 )Ver juegos ( 2 )Ver Ventas ( 3 )Ver Clientes ( 4 )Top Ventas ( 5 )Total ventas ( 0 )Terminar programa ==> ", 'blue')
        option_menu = str(input(menu))

        if option_menu == "1":
            listar_juegos()
        elif option_menu == "2":
            listar_ventas()
        elif option_menu == "3":
            listar_clientes()
        elif option_menu == "4":
            top_ventas()
        elif option_menu == "5":
            print(c(f"\n[+] Juegos vendidos: {ventas_totales()} unidades ", 'cyan'))
        elif option_menu == "0":
            terminar_programa()
        else:
            print(c("\n[-] Opcion no valida, Elige una opcion correcta...", 'red'))

# Flujo principal de tiendaGamer 
if __name__ == "__main__":
    main()
