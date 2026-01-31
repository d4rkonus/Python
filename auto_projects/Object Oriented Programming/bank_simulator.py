#!/usr/bin/python3

class BankAccount:
    def __init__(self, account_name, account_number, balance=0):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"\n[+] Money deposited: {money}€.")
        print(f"\n[+] New balance: {self.balance}€.")

    def withdraw(self, money):
        if money > self.balance:
            return("\n[!] Warning: Insufficient funds!")    

        self.balance -= money
        print(f"\n[-] Money withdrawn: {money}€.")
        print(f"\n[-] New balance: {self.balance}€.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("[!] Enter a positive amount.")
                continue
            return value
        except ValueError:
            print("[!] Invalid number. Try again.")


def main():
    print("=== Bank Simulator ===")
    name = input("Account name: ")
    number = input("Account number: ")
    account = BankAccount(name, number)

    
    while True:
        try:
            print("\n1) Deposit\n2) Withdraw\n3) Balance\n4) Exit")
            option = input("Choose an option: ").strip()

            if option == "1":
                amount = get_positive_float("Amount to deposit: ")
                account.deposit(amount)

            elif option == "2":
                amount = get_positive_float("Amount to withdraw: ")
                warning = account.withdraw(amount)
                if warning:
                    print(warning)

            elif option == "3":
                print(f"\n[=] Current balance: {account.balance}€.")


            elif option == "4": 
                print("\nGoodbye!")
                break
            else:
                print("[!] Invalid option. Try again.")

        except KeyboardInterrupt:
            print(f"\n Moving to safe zone...")
            break

if __name__ == "__main__":
    main()

        
