#!/usr/bin/python3

import re

print("\n[+] Opciones disponibles: ")

print("\n1) Palabras repetidas")
print("2) Letras repetidas (mayus y minus)")
print("3) Numeros individuales repetidos")
print("4) Numeros conjuntos repetidos")
print("5) Combinación letras y numeros repetidos")

option = input("\n[+] Selecciona opción: ")

if option == "1":
    words = input("\n[$] Introduce las palabras: ")
    matcher_1 = re.finditer(r"\b(\w+)\s+\1\b", words, re.IGNORECASE)
    print([m.group() for m in matcher_1])
elif option == "2":
    words = input("\n[$] Introduce las palabras: ")
    matcher_2 = re.finditer(r"([a-zA-Z])\1", words, re.IGNORECASE)
    print([m.group() for m in matcher_2])

elif option == "3":
    numbers = input("\n[$] Introduce los numeros: ")
    matcher_3 = re.search(r"(\d)\1+", numbers)
    if matcher_3:
        print("Número repetido:", matcher_3.group(1))
    else:
        print("No hay números repetidos como bloque.")

    
elif option == "4":
    numbers = input("\n[$] Introduce los numeros: ")
    matcher_4 = re.finditer(r"\b(\d+)\s+\1\b", numbers)
    print([m.group() for m in matcher_4])

elif option == "5":
    combo = input("\n[$] Introduce texto combinado: ")
    matcher_5 = re.finditer(r"([a-zA-Z0-9])\1", combo, re.IGNORECASE)
    print([m.group() for m in matcher_5])

else:
    print("\n[!] Opción no permitida")