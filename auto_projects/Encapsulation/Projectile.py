#!/usr/bin/python3

class Tank:
    def __init__(self, proyectil):
        if proyectil <= 0:
            raise ValueError("No tienes munición :(")
        self.__proyectil = proyectil
    
    def recargar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("No se recargó ningún proyectil.")
        self.__proyectil += cantidad

    def disparar(self, cantidad=1):
        if cantidad <= 0:
            raise ValueError("No hay munición.")
        if cantidad > self.__proyectil:
            raise ValueError("No tienes suficiente munición.")
        self.__proyectil -= cantidad

    def ver(self):
        return self.__proyectil


def main():
    try:
        mete_munición = float(input("\nInserta proyectiles: "))
        cuenta = Tank(mete_munición)

        while True:
            print("\n1. Recargar")
            print("2. Disparar")
            print("3. Ver munición")
            print("4. Salir")

            opcion = input("\n[+] Elige una opción: ")

            try:
                if opcion == "1":
                    cantidad = int(input("Cantidad a recargar: "))
                    cuenta.recargar(cantidad)

                elif opcion == "2":
                    cantidad = int(input("Cantidad a retirar: "))
                    cuenta.disparar(cantidad)

                elif opcion == "3":
                    print("Munición actual:", cuenta.ver())

                elif opcion == "4":
                    break

                else:
                    print("Opción inválida")

            except ValueError as e:
                print("Error:", e)

    except KeyboardInterrupt:
        print("\n\n[!] Moving to safe zone...\n\n")


if __name__ == "__main__":
    main()