#!/usr/bin/python3

class Money:
    def __init__(self, quantity, value):
        self.quantity = quantity
        self.value = value

    def __repr__(self):
        return f"{self.quantity} bill(s) of {self.value}€"
    
class Money_factory:
    # total de billetes y dinero total creado
    bills_created = {}
    total_money = 0

    @staticmethod
    # tipos de valores que se pueden poner en billetes
    def types_of_value(value):
        return value in [5, 10, 20, 50, 100, 200, 500]

    @classmethod
    def create_bills(cls, value, quantity):
        if not cls.types_of_value(value):
            raise ValueError("Type of value not allowed.")
        
        if quantity <= 0:
            raise ValueError("Give me more quantity than 0.")
    
        # contar billetitos
        if value in cls.bills_created:
            cls.bills_created[value] += quantity
        else:
            cls.bills_created[value] = quantity

        # sumalo todo
        cls.total_money += value * quantity
        print(cls.total_money)
    
    @classmethod
    def show_info(cls):
        print("\n📊 MONEY FACTORY")
        print("------------------------")

        for value, quantity in sorted(cls.bills_created.items()):
            print(f"{quantity} bill(s) of {value}€ → {quantity * value}€")

        print("------------------------")
        print(f"💰 TOTAL MONEY: {cls.total_money}€\n")

## De aquí para arriba, actua por detras, es pura lógica

def main():
    while True:
        try:
            value = int(input("Give me the bill value: "))
            quantity = int(input("Give me the quantity of bills: "))

            Money_factory.create_bills(value, quantity)
            print("[+] Bills created nicely :)")

        except KeyboardInterrupt:
            print(f"\n[!] Moving to safe zone.")
            break

        except ValueError as a:
            print(f"[!] Error {a}")
            continue

        additional_option = input("Add more bills? (y/n): ").lower()
        if additional_option != "y":
            break

    Money_factory.show_info()


if __name__ == "__main__":
    main()