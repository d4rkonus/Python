#!/usr/bin/python3

while True:
    try:
        numbers = []
        number = input("\nGive me the numbers: ")

        for number in number.split():
            numbers.append(int(number))

        max = numbers[0]
        min = numbers[0]

        for number in numbers:
            if number > max:
                max = number
            if number < min:
                min = number

    except KeyboardInterrupt:
        print("\n\n[!] Moving to safe zone...")
        break
    
    unique_numbers = list(set(numbers))

    print(f"\nThe biggest number is: {max}")
    print(f"\nThe smallest number is {min}")