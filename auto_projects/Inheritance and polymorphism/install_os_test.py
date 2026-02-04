#!/usr/bin/python3

import time
import os

class OperatingSystem:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def install_os(self):
        time.sleep(1)
        print(f"\n[+] Installing {self.name} version {self.version}...")
        time.sleep(1)
        print("[+] Installation complete!")
        time.sleep(2)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

class Windows11(OperatingSystem):
    def __init__(self):
        super().__init__("Windows", "11")

class Windows10(OperatingSystem):
    def __init__(self):
        super().__init__("Windows", "10")

class WindowsXP(OperatingSystem):
    def __init__(self):
        super().__init__("Windows", "XP")

class Ubuntu(OperatingSystem):
    def __init__(self):
        super().__init__("Ubuntu", "24.04")

while True:
    try:
        print("\nWhich operating system do you want to install? ")
        print("1. Windows 11")
        print("2. Windows 10")
        print("3. Windows XP")
        print("4. Ubuntu 24.04")
        choice = int(input("\nGive me the number: "))
        if choice == 1:
            w11 = input("\nReady to install pure cheap IA and things that you dont need? --> ")
            if w11 == "yes" or w11 == "y":
                    time.sleep(1)
                    w11_installing = Windows11()
                    w11_installing.install_os()
                    time.sleep(1)
                    w11_installing.clear_screen()
            else:
                print("\n[!] Installation cancelled.")
        elif choice == 2:
            w10 = input("\nReady to install a Windows 11 without IA and bullshit adds? --> ").lower()
            if w10 == "yes" or w10 == "y":
                    time.sleep(1)
                    w10_installing = Windows10()
                    w10_installing.install_os()
                    time.sleep(1)
                    w10_installing.clear_screen()
            else:
                print("\n[!] Installation cancelled.")
                time.sleep(1)
                w10_installing.clear_screen()

        elif choice == 3:
            wxp = input("\nReady to install the old but gold Windows XP? --> ").lower()
            if wxp == "yes" or wxp == "y":
                    time.sleep(1)
                    wxp_installing = WindowsXP()
                    wxp_installing.install_os()
                    time.sleep(1)
                    wxp_installing.clear_screen()
            else:
                    print("\n[!] Installation cancelled.")
                    time.sleep(1)
                    wxp_installing.clear_screen()
    
        elif choice == 4:
            ubu = input("\nReady to install the best os of the list? --> ").lower()
            if ubu == "yes" or ubu == "y":
                    time.sleep(1)
                    ubu_installing = Ubuntu()
                    ubu_installing.install_os()
                    time.sleep(1)
                    ubu_installing.clear_screen()
            else:
                print("\n[!] Installation cancelled.")
                time.sleep(1)
                ubu_installing.clear_screen()


        else:
            print("\n[-] Invalid choice. Please select a valid option.")

    except ValueError:
        print("\n[-] Invalid input. Please enter a number corresponding to your choice.")

    except KeyboardInterrupt:
        print("\n[+] Moving to safe zone...")
        break

