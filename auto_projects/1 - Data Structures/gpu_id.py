#!/usr/bin/python3

import time
import os

def create_gpus(brand, model, id_number):
    return f"""
      [+] GPU Brand: {brand}
      [+] Model: {model} 
      [+] ID: {id_number:06d}
    """

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

gpus_set = set()

def main_function():
    while True:
        try:
            show_main_panel()
            print("=== GPU Information Collector ===")

            print("\nAvailable Options:")
            print("1) Check gpus collected")
            print("2) Add new gpu")
            print("3) Exit")

            option = int(input("\nSelect an option (1-3): "))

            if option == 1:
                check_gpus_collected()
                if not gpus_set:
                    print("\n[!] No GPUs collected yet.")
                input("\nPress Enter to continue...")
                clear_screen()
            elif option == 2:
                add_new_gpu()
                input("\nPress Enter to continue...")
                clear_screen()
            elif option == 3:
                print("\n[!] Moving out ...")
                clear_screen()
                break
            else:
                print("Select a valid option (1-3).")

        except KeyboardInterrupt:
            print("\n Moving to safe zone ...")
            break
        except ValueError:
            print(" Please enter a valid number (1-3).")


def show_main_panel():
    clear_screen()


def check_gpus_collected():
    for gpu in gpus_set:
        print(gpu)


def add_new_gpu():
    brand = input("GPU Brand: ")
    if brand.lower() not in {"nvidia", "amd", "intel"}:
        print("\n[!] Invalid GPU brand. Brand does not exist.")
        return

    model = input("GPU Model: ")
    try:
        id_number = int(input("GPU ID (number): "))
    except ValueError:
        print("\n[!] Invalid ID. Please enter a valid number.")
        return

    gpus_set.add(create_gpus(brand, model, id_number))
    print("\n[+] GPU added successfully!")
    time.sleep(2)


# Start the program
if __name__ == "__main__":
    main_function()    