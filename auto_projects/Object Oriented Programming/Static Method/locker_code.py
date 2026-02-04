#!/usr/bin/python3

class Locker:
    def __init__(self, locker_number, locker_code=4320):
        self.locker_number = locker_number
        self.locker_code = locker_code
        self.is_open = False

    @staticmethod
    def open_locker(locker, input_code):
        if input_code == locker.locker_code:
            locker.is_open = True
            return True
        return False
        
locker_number = input("Enter locker number: ")
locker = Locker(locker_number)

while True:
    try:
        input_code = int(input("Enter locker code to open: "))
        if Locker.open_locker(locker, input_code):
            print("\n[+] Access granted.")
            print(f"\n[+] Locker {locker.locker_number} opened successfully!")
            break
        else:
            print("\nIncorrect code. Try again.")
        
    except KeyboardInterrupt:
        print("\n\n[!] Moving to safe zone ...")
        break

    except ValueError:
        print("\n[!] Please enter a valid numeric code.")

