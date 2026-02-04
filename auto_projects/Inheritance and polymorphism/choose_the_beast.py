#!/usr/bin/python3

import os
import time


class Beast:
    def __init__(self, name, land, element, enemy):
        self.name = name
        self.land = land
        self.element = element
        self.enemy = enemy

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def describe(self):
        print(f"""
[+] You are going to {self.land}
    Be aware! You will need to fight
    with a {self.enemy} called {self.name}.
""")


class Rudania(Beast):
    def __init__(self):
        super().__init__(
            name="Rudania",
            land="Fire Mountain",
            element="Fire",
            enemy="giant robot lizard"
        )


class Naboris(Beast):
    def __init__(self):
        super().__init__(
            name="Naboris",
            land="Lightning Desert",
            element="Electricity",
            enemy="giant robot camel"
        )


class Medoh(Beast):
    def __init__(self):
        super().__init__(
            name="Medoh",
            land="Wind Valley",
            element="Wind",
            enemy="giant robot bird"
        )


class Ruta(Beast):
    def __init__(self):
        super().__init__(
            name="Ruta",
            land="Water Palace",
            element="Water",
            enemy="giant robot elephant"
        )


def main():
    beasts = {
        1: Rudania(),
        2: Naboris(),
        3: Medoh(),
        4: Ruta()
    }

    while True:
        try:
            print("\n[?] What do you most prefer?")
            print("1. Go to fire paradise.")
            print("2. Have a luxurious tan.")
            print("3. Do eternal skydiving.")
            print("4. Swim in the water kingdom.")
            print("0. Exit")

            answer = int(input("\nGive me the number: "))

            if answer == 0:
                print("\n[+] Goodbye, hero!")
                break

            beast = beasts.get(answer)

            if not beast:
                print("\n[!] Please select a valid option.")
                time.sleep(1)
                continue

            time.sleep(1)
            beast.describe()

            input("\n[+] Press ENTER to return to the main menu...")
            beast.clear_screen()

        except ValueError:
            print("\n[!] Please enter a valid number.")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        except KeyboardInterrupt:
            print("\n[!] Moving to safe zone ...")
            break

if __name__ == "__main__":
    main()
