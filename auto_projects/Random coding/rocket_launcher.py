#!/usr/bin/python3

import os
import time

class Rocket:
    def __init__(self, id_rocket, model_rocket, brand, status):
        self.id_rocket = id_rocket
        self.model_rocket = model_rocket
        self.brand = brand
        self.status = status


    def show_info(self, delay=1):
        info = [
            f"\n[+] Rocket ID: {self.id_rocket}",
            f"[+] Model: {self.model_rocket}",
            f"[+] Brand: {self.brand}",
            f"[+] Status: {self.status}",
        ]

        for line in info:
            print(line)
            time.sleep(delay)


def panel():
    print(f"\n======Rocket Launcher Simulator======")
    print(f"\nOptions available:")
    print(f"1. Show me the brands and models.")
    print(f"2. Show me all the list of rockets.")
    print(f"3. Add new rocket to the list.")
    print(f"4. Exit the program.")

def show_brands_models(rockets):
    print(f"\n- Let me show you the different brands and models of rockets available: \n")
    for rocket in rockets:
            time.sleep(1)
            print(f"[+] Brand: {rocket.brand}")
            print(f"[+] Model: {rocket.model_rocket}\n")
            

def rockets_full(rockets):
     for rocket in rockets:
          rocket.show_info(delay=1)

rockets_list = [
    Rocket(100, "Vengator 01", "Space 4 life", "Ready to take off"),
    Rocket(101, "Vengator 02", "Space 4 life", "On the way to the moon."),
    Rocket(102, "Lumis 00X", "SpaceX", "Beeing repaired.")
    ]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        while True:
            panel()
            option = input("\n[+] Give me an option: ")
            if option == "1":
                clear_screen()
                show_brands_models(rockets_list)
                print(f"\n[+] Press Enter to continue...")
                input()
                clear_screen()
            elif option == "2":
                clear_screen()
                print(f"\n- Let me show you the list of rockets: \n")
                rockets_full(rockets_list)
                print(f"\n[+] Press Enter to continue...")
                input()
                clear_screen()
            elif option == "3": 
                new_rocket_id = int(input("\n[+] Give me the rocket ID: ")) 
                new_rocket_model = input("[+] Give me the rocket model: ")
                new_rocket_brand = input("[+] Give me the rocket brand: ")
                new_rocket_status = input("[+] Give me the rocket status: ")

                ### Adding the new rocket to he list
                new_rocket = Rocket(new_rocket_id, new_rocket_model, new_rocket_brand, new_rocket_status) 
                rockets_list.append(new_rocket)

                print(f"\n[+] New rocket {new_rocket_id} added to the list.")
                print(f"\n[+] Press Enter to continue...")
                input()
                clear_screen()
            elif option == "4":
                print(f"\n[?] Leaving the program.")
                break

            else:   
                print(f"\n[!] Invalid option. Please try again.")   

    except KeyboardInterrupt:
        print(f"\n\n[!] Moving to safe zone... ")


if __name__ == "__main__":
    main()
