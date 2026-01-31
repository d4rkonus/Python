#!/usr/bin/python3
        
class BankAccount:
    def __init__(self, account_name, account_number, money=0):
        self.account_name = account_name
        self.account_number = account_number
        self.money = money

    
    def deposit_money(self, money):
        self.money += money
        return(f"\nNew money deposited: {money}€")
        return(f"\nTotal money in the account: {self.money}€")
    
    def withdraw_money(self, money):

        if money > self.money:
            return("\nYou don't have enough money in your account.")
            return("\nPut more money to start operate. Fucking poor.")
        
        self.money -= money
        return(f"\nYou did a withdrawn with {money}€")
        return(f"\nTotal money in the account: {self.money}€")
    
    def give_me_money(self, message):
        while True:
            try:
                value = float(input(message))
                if value <= 0:
                    print("Give me a positive amount of money.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Enter a numeric value.")
                
name = input("Enter account name: ")
number = input("Enter account number: ")

account_info = BankAccount(name, number)

while True:
    try:
        print("\n1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Exit")

        option = input("Choose an option: ").strip()

        if option == '1':
            amount = account_info.give_me_money("Enter amount to deposit: ")
            print(account_info.deposit_money(amount))