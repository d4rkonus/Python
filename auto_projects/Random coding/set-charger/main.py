#!/usr/bin/python3

import os
from loader import equip_and_progress

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    print("\n[+] You have 3 types of vehicle to choose: ")
    print("\n1) Air vehicle")
    print("\n2) Land vehicle")
    print("\n3) Marine vehicle")

    number = int(input("\nWhich type of vehicle you want:  "))


    if number == 1:
        clear_screen()
        print("\nOkay, so you want an Air Vehicle.")
        print("\n[+] Feel free to choose:")
        print("\n1) Dark Clown Cruiser")
        print("\n2) Jet Stream")
        print("\n3) Sky Slicer")

        air_veh = int(input("\nChoose a model:  "))

        if air_veh == 1:
            weapons = [
                "Cruise propulsion",
                "Iron figurehead",
                "Koopa bombers"
            ]
        
            equip_and_progress(weapons)

        if air_veh == 2:
            weapons = [
                "Brass feather wings"
                "Fly control"
                "Aerial blades"
            ]
            
            equip_and_progress(weapons)

        if air_veh == 3:
            weapons = [
                "Iron structure"
                "Double edge hull"
                "Feather fury"   
            ]

            equip_and_progress(weapons)
    
    if number == 2:
        clear_screen()
        print("\nOkay, so you want an Land Vehicle.")
        print("\n[+] Feel free to choose:")
        print("\n1) Dark Hot Streak")
        print("\n2) Shark Tank")
        print("\n3) Shield Striker")

        lan_veh = int(input("\nChoose a model:  "))

        if lan_veh == 1:
            weapons = [
                "Blaze boosters",
                "Blue fire wheels",
                "Fire grill"
            ]
        
            equip_and_progress(weapons)

        if lan_veh == 2:
            weapons = [
                "Terrafin turbo",
                "Caterpillar tracks",
                "Ballistic cannons"
            ]
            
            equip_and_progress(weapons)

        if lan_veh == 3:
            weapons = [
                "Iron structure",
                "Double edge hull",
                "Feather fury"   
            ]

            equip_and_progress(weapons)

    if number == 3:
        clear_screen()
        print("\nOkay, so you want an Marine Vehicle.")
        print("\n[+] Feel free to choose:")
        print("\n1) Sea shadow")
        print("\n2) Dive bomber")
        print("\n3) Deep reeper")

        mar_veh = int(input("\nChoose a model:  "))

        if mar_veh == 1:
            weapons = [
                "Chasm turbine"
                "Dark manta fins"
                "Abyss cannon"
            ]

            equip_and_progress(weapons)

        if mar_veh == 2:
            weapons = [
                "Deep dynamo"
                "Submarine radar"
                "Deep turpedo guns"
            ]

            equip_and_progress(weapons)

        if mar_veh == 3:
            weapons = [
                "Tidal turbine"
                "Ice guns"
                "Trident head"
            ]

            equip_and_progress(weapons)
except KeyboardInterrupt:
    print("\n[!] Moving to safe zone...")