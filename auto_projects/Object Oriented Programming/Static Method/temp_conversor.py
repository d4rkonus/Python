#!/usr/bin/python3

class Conversor:

    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5/9
    
while True:
    try:
        choice = input("\nChoose conversion (1: C to F, 2: F to C): ")
        
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = Conversor.c_to_f(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = Conversor.f_to_c(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        
        else:
            print("Invalid choice. Please select 1 or 2.")
    
    except KeyboardInterrupt:
        print("\n[!] Moving to safe zone ...")
        break
    
    except ValueError:
        print("Please enter a valid numeric temperature.")
