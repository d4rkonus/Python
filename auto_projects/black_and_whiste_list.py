#!/usr/bin/python3
import os
import time

# Fixed data structure: Using dictionaries instead of mixed sets
whitelist_devices = {
    "Device 1": {"Type": "Smartphone", "Model": "iPhone 17 Pro Max", "MAC": "3A:7F:C2:91:4D:E8"},
    "Device 2": {"Type": "Smartphone", "Model": "Samsung Galaxy S23", "MAC": "8C:14:B9:6E:53:2A"},
    "Device 3": {"Type": "Tablet", "Model": "iPad Pro 12.9", "MAC": "D2:5B:0A:EF:39:71"},
    "Device 4": {"Type": "Laptop", "Model": "MacBook Pro 16", "MAC": "4E:A3:7C:18:92:BD"},
    "Device 5": {"Type": "Laptop", "Model": "Asus ROG Zephyrus G14", "MAC": "9A:60:F4:2D:C8:05"}
}

blacklist_devices = {
    "Device 1": {"Type": "Laptop", "Model": "Acer Aspire 5", "MAC": "1B:2C:3D:4E:5F:60"},
    "Device 2": {"Type": "Smartphone", "Model": "Motorola Moto G Power", "MAC": "A1:B2:C3:D4:E5:F6"},
    "Device 3": {"Type": "Tablet", "Model": "Samsung Galaxy Tab S8", "MAC": "11:22:33:44:55:66"},
    "Device 4": {"Type": "Console", "Model": "PlayStation 5", "MAC": "AA:BB:CC:DD:EE:FF"},
    "Device 5": {"Type": "Console", "Model": "Nintendo Switch 2", "MAC": "99:88:77:66:55:44"}
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_main_panel():
    clear_screen()
    print("=== Device Management System ===")

def white_devices_collected():
    print("\n[-] Use devices on whitelist:")
    for device_id, info in whitelist_devices.items():
        print(f"  > {device_id}: {info['Type']} - {info['Model']} (MAC: {info['MAC']})")

def black_devices_collected():
    print("\n[-] Use devices on blacklist:")
    for device_id, info in blacklist_devices.items():
        print(f"  > {device_id}: {info['Type']} - {info['Model']} (MAC: {info['MAC']})")

def add_new_device():
    print("\n[-] Add New Device")
    name = f"Device {len(whitelist_devices) + 1}"
    
    dev_type = input("Device Type (e.g., Smartphone): ")
    model = input("Device Model: ")
    mac = input("MAC Address: ")
    
    whitelist_devices[name] = {"Type": dev_type, "Model": model, "MAC": mac}
    print(f"\n[+] {name} added successfully!")

def main_function():
    while True:
        try:
            show_main_panel()
            
            print("\nAvailable options:")
            print("1) Check whitelist devices")
            print("2) Add new device")
            print("3) Check blacklist devices")
            print("4) Exit")

            try:
                option = int(input("\nSelect an option (1-4): "))
            except ValueError:
                print("\n[!] Please enter a valid number.")
                time.sleep(1)
                continue

            if option == 1:
                white_devices_collected()
                if not whitelist_devices:
                    print("\n[!] No devices collected yet.")
                white_use = int(input("\nGive the number of the device you want to use: "))
                print(f"\n[+] You are using the device correctly and you are free to use it with no restrictions.")
                time.sleep(1)
                input("\nPress Enter to continue...")


            elif option == 2:
                add_new_device()
                time.sleep(1)
                input("\nPress Enter to continue...")
            
            elif option == 3:
                black_devices_collected()
                if not blacklist_devices:
                    print("\n[!] No devices collected yet.")
                black_use = int(input("\nGive the number of the device you want to use: "))
                print(f"\n[!] You are using the device incorrectly, wait while we block it and call the police.")
                time.sleep(1)
                input("\nPress Enter to continue...")

            elif option == 4:
                print("\n[!] Moving out...")
                break
            
            else:
                print("\n[!] Select a valid option (1-4).")
                time.sleep(1)

        except KeyboardInterrupt:
            print("\n\n[!] Moving to safe zone...")
            break

if __name__ == "__main__":
    main_function()
