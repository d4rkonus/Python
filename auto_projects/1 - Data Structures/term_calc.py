#!/usr/bin/python3

def check_operation(operation):
    for character in operation:
        if character not in "0123456789+-*/(). ":
            raise ValueError("Select correct character.")


def calculate(operation):
    check_operation(operation)
    return eval(operation)


while True:
    try:
        operation = input("\nGive me the full operation: ")
    
        result = calculate(operation)

    except ZeroDivisionError:
        print("Error: división entre cero")

    except KeyboardInterrupt:
        print("\n[!] Moving to safe zone ...")
        break

    else:
        print("Result:", result)