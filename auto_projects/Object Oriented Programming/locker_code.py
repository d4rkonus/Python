#!/usr/bin/python3

class Locker:
    def __init__(self, locker_number, locker_code=4320):
        self.locker_number = locker_number
        self.locker_code = locker_code

    def open_locker(self, input_code):
        if input_code == self.locker_code:
            return f"\nLocker {self.locker_number} is now open."
        else:
            return "\nIncorrect code. Access denied."
        
locker_number = input("Enter locker number: ")
locker = Locker(locker_number)

while True:
    try:
        input_code = int(input("Enter locker code to open: "))
        print(locker.open_locker(input_code))
    except ValueError:
        print("Please enter a valid numeric code.")
    except KeyboardInterrupt:
        print("\n\nExiting...")
        break