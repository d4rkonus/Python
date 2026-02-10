#!/usr/bin/python3

class CuentaBancaria:
    def __init__(self, saldo):
        if saldo < 0:
            raise ValueError("Empiezas con 0 en la cuenta :(")
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad inválida.")
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= 0 or cantidad > self.__saldo:
            raise ValueError("No tienes suficientes fondos para retirar")
        self.__saldo -= cantidad

    def ver(self):
        return self.__saldo
    

def main():
    try:
        saldo_inicial = float(input("\nDame el saldo inicial: "))
        cuenta = CuentaBancaria(saldo_inicial)

        while True:
            print("\n1. Depositar")
            print("2. Retirar")
            print("3. Ver saldo")
            print("4. Salir")

            opcion = input("\n[+] Elige una opción: ")

            try:
                if opcion == "1":
                    cantidad = float(input("Cantidad a depositar: "))
                    cuenta.depositar(cantidad)

                elif opcion == "2":
                    cantidad = float(input("Cantidad a retirar: "))
                    cuenta.retirar(cantidad)

                elif opcion == "3":
                    print("Saldo actual:", cuenta.ver())

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
