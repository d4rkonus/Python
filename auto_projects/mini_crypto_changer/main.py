#!/usr/bin/python3

import requests

from eur_btc import eur_btc
from eur_eth import eur_eth
from eur_doge import eur_doge

MENU = {
    "1": ("BTC", eur_btc),
    "2": ("ETH", eur_eth),
    "3": ("DOGE", eur_doge),
}


while True:
    print("\n[+] Which price do you want to check?")
    for index_number, (coin, _) in MENU.items():
        print(f"{index_number}. EUR to {coin}")
    print("q. Quit")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "q":
        print("Goodbye!")
        break

    if choice not in MENU:
        print("[!] Invalid choice. Please select a valid option.")
        continue

    while True:
        try:
            eur_amount = float(input("Enter amount in EUR: ").strip())
            break
        except ValueError:
            print("Please enter a valid numeric amount.")

    coin, converter = MENU[choice]

    try:
        result = converter(eur_amount)
        print(f"{eur_amount} EUR ≈ {result:.8f} {coin}")
    except requests.RequestException as exc:
        print(f"Could not fetch {coin} price: {exc}")