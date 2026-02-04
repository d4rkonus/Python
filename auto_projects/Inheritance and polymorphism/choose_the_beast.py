#!/usr/bin/python3

import os 
import time


class Beast:
    def __init__(self, name, land, element):
        self.name = name
        self.land = land
        self.element = element

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def go_to_land(self):
        print(f"\n[?] What do you most prefer?")
        print(f"1. Go to fire paradaise.")
        print(f"2. Have a luxurious tan .")
        print(f"3. Do eternal skydiving .")
        print(f"4. Swim in the water kingdom.")

        answer = int(input("\nGive me the number: "))

        if answer == 1:
            time.sleep(1)
            print(f"""\n
                  [+] You are going to {self.land} but be aware, 
                      you will need to fight with a giant robot lizard called {self.name.Beast()}.""")

        elif answer == 2:
            time.sleep(1)
            print(f"""\n
                  [+] You are going to {self.land} but be aware, 
                      you will need to fight with a giant robot camel called {self.name.Beast()}.""")

        elif answer == 3:
            time.sleep(1)
            print(f"""\n
                  [+] You are going to {self.land} but be aware, 
                      you will need to fight with a giant robot bird called {self.name.Beast()}.""")
            
        elif answer == 4:
            time.sleep(1)
            print(f"""\n
                  [+] You are going to {self.land} but be aware, 
                      you will need to fight with a giant robot elephant called {self.name.Beast()}.""")
            
        else: 
            print("\n[!] Please select some land to visit.")

    
class Rudania(Beast):
    def __init__(self):
        super().__init__("Rudania", "Fire Mountain", "Fire")

class Naboris(Beast):
    def __init__(self):
        super().__init__("Naboris", "Lightning Desert", "Electricity")

class Medoh(Beast):
    def __init__(self):
        super().__init__("Medoh", "Wind Valley", "Wind")

class Ruta(Beast):
    def __init__(self):
        super().__init__("Ruta", "Water Palace", "Water")