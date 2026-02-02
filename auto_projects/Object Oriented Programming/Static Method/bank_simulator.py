#!/usr/bin/python3
        
import time

class BankAccount:

    @staticmethod
    def deposit(balance, amount):
        return balance + amount
    
    @staticmethod
    def withdraw(balance, amount):
        if amount > balance:
            print("\n[!] Not enought money.")
            return balance
        return balance - amount
    
    @staticmethod
    def give_money(msg):
        while True:
            try:
                value = float(input(msg))
                if value <= 0:
                    print("[!] Please put positive number.")
                    continue
                return value
            except ValueError:
                print("\n[-] Invalid Number.")

balance = 0

while True:
    print("\n1) Deposit\n2) Withdraw\n3) Balance\n4) Exit")
    option = input("Choose: ")

    if option == "1":
        balance = BankAccount.deposit(balance, BankAccount.give_money("Deposit: "))
    elif option == "2":
        balance = BankAccount.withdraw(balance, BankAccount.give_money("Withdraw: "))
    elif option == "3":
        print("Balance:", balance)
    elif option == "4":
        break