#!/usr/bin/python3
from datetime import date

try:
    dia = int(input("\nDía de nacimiento: "))
    mes = int(input("Mes de nacimiento: "))
    año = int(input("Año de nacimiento: "))

    if año < 1900: 
        raise ValueError("El año es muy antiguo") # No deberia estar vivo
    
    if mes < 1 or mes > 12:
        raise ValueError("El mes no existe.")
    
    if dia < 1 or dia > 31:
        raise ValueError("El dia no existe.")
    
    fecha_nacimiento = date(año, mes, dia)

    hoy = date.today()

    if fecha_nacimiento > hoy:
        raise ValueError("Eres viajero de tiempo?")
    
    # Se calcula la edad exacta
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

except ValueError as error:
    print("Error:", error)

except KeyboardInterrupt:
    print("\n\n[!] Saliendo a zona segura ...")

else:
    print("\n\n[$] La edad exacta es:", edad, "años")

finally:
    print("\nPrograma finalizado ...")