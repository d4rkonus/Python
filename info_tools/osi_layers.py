#!/usr/bin/python3

from colorama import Fore
import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def presentation():
    print("\nAsí que quieres saber todas las capas del modelo OSI.")
    time.sleep(1)
    print("\nVamos paso a paso, te contaré detalles de cada capa:")

    print("\n[+] Presiona 'Enter' para continuar.")
    input()
    clear_screen()
    
def capa_fisica(delay=1):
    mensajes = [
        "1 - Capa física",
        "Esta capa más profunda de todas, tiene la función de servir como transmisora de datos a través de un medio físico de la red.",
        "En otras palabras, es el camino físico que usan los paquetes para llegar al destino.",
        "[+] Ejemplos sencillos de capa física:",
        " · Cables de cobre",
        " · Fibra óptica"
    ]
    
    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)
    
    input("\n[+] Presiona 'Enter' para seguir.")


def capa_enlace(delay=1):
    mensajes = [
        "2 - Capa de enlace de datos", 
        "Esta capa tiene la función de checkear el estado de los paquetes que se van a transmitir, comprueba si tienen errores y los corrige si es posible.",
        "Una vez los paquetes salen de esta capa, se consideran 'aprobados' para las siguientes capas."
    ]

    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)

    input("\n[+] Presiona 'Enter' para seguir.")


def capa_red(delay=1):
    mensajes = [
        "3 - Capa de red",
        "Esta capa se encarga de la transferencia confiable de paquetes entre dispositivos usando múltiples redes.",
        "Usando direcciones lógicas e IP, decide cuál es el mejor camino para los paquetes."
    ]

    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)
        
    input("\n[+] Presiona 'Enter' para seguir.")
        

def capa_transporte(delay=1):
    mensajes = [
        "4 - Capa de transporte", 
        "Transporta los paquetes de forma confiable entre dispositivos.",
        "Ofrece control de flujo y corrección de errores."
    ]

    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)

    input("\n[+] Presiona 'Enter' para seguir.")


def capa_sesion(delay=1):
    mensajes = [
        "5 - Capa de sesión", 
        "Crea y mantiene sesiones de comunicación entre dispositivos.",
        "Gestiona autenticación y confirmación."
    ]   

    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)
    
    input("\n[+] Presiona 'Enter' para seguir.")
        

def capa_presentacion(delay=1):
    mensajes = [
        "6 - Capa de presentación", 
        "Traduce los datos a un formato entendible por la capa de aplicación.",
        "Realiza cifrado, compresión y codificación."
    ]

    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)
    
    input("\n[+] Presiona 'Enter' para seguir.")


def capa_aplicacion(delay=1):
    mensajes = [
        "7 - Capa de aplicación", 
        "Muestra los datos al usuario final a través de aplicaciones.",
        "Gracias a esta capa usamos email, navegadores web, etc."
    ]

    for mensaje in mensajes:
        print(f"\n{mensaje}")
        time.sleep(delay)
    
    input("\n[+] Presiona 'Enter' para seguir.")


# =========================
# EJECUCIÓN SEGURA
# =========================

hide_cursor()

try:
    presentation()
    capa_fisica()
    capa_enlace()
    capa_red()
    capa_transporte()
    capa_sesion()
    capa_presentacion()
    capa_aplicacion()

except KeyboardInterrupt:
    print(Fore.RED + "\n\n[!] Programa interrumpido por el usuario.")

finally:
    show_cursor()
    print("\nCursor restaurado correctamente.")
