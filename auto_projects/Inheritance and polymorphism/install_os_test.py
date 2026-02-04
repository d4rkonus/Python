#!/usr/bin/python3

import os


class OperatingSystem:
    def __init__(self, name, version):
        self.name = name
        self.version = version


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

def install_os(self):
    print(f"\n[+] Installing {self.name} version {self.version}...")
    print("[+] Installation complete!")

while True:
    try:
        print("\nWhich operating system ")
        print("1. Windows 11")
        print("2. Windows 10")
        print("3. Windows XP")
        print("4. Ubuntu 24.04")
        choice = int(input("Give me the number: "))
        if choice == 1:
            w11 = input("\nReady to install pure cheap IA and things that you dont need?").lower()
            if w11 == "yes" or w11 == "y":
                    w11_installing = Windows11()
                    install_os(w11_installing)
            else:
                print("Installation cancelled.")
        elif choice == 2:
            w10 = input("\nReady to install a Windows 11 without IA and bullshit adds?").lower()
            if w10 == "yes" or w10 == "y":
                    w10_installing = Windows10()
                    install_os(w10_installing)
            else:
                print("Installation cancelled.")

        elif choice == 3:
            wxp = input("\nReady to install the old but gold Windows XP?").lower()
            if wxp == "yes" or wxp == "y":
                    wxp_installing = WindowsXP()
                    install_os(wxp_installing)
            else:
                    print("Installation cancelled.")

        elif choice == 4:
            ubu = input("\nReady to install the best os of the list? ").lower()
            if ubu == "yes" or ubu == "y":
                    ubu_installing = Ubuntu()
                    install_os(ubu_installing)
            else:
                print("Installation cancelled.")


        else:
            print("[-] Invalid choice. Please select a valid option.")

    except ValueError:
        print("[-] Invalid input. Please enter a number corresponding to your choice.")

    except KeyboardInterrupt:
        print("\n[+] Moving to safe zone...")
        break


install_os()

