#!/usr/bin/python3

import time


class Weapon:
    def __init__(self, model, power, damage):
        self.model = model
        self.power = power
        self.damage = damage


class Warrior:
    def __init__(self, name, strength, weapon):
        self.name = name
        self.strength = strength
        self.weapon = weapon

 
# --- Weapon Instances ---
axe = Weapon("axe", "ice", 50)
hammer = Weapon("hammer", "lightning", 80)
sword = Weapon("sword", "fire", 70)
spear = Weapon("spear", "air", 40)
globes = Weapon("globes", "rock", 45)


# --- Warriors Instances ---
lancelot = Warrior("lancelot", 70, spear)
surtr = Warrior("surtr", 90, sword)
bercox = Warrior("bercox", 60, axe)
navinni = Warrior("navinni", 50, globes)
nexus = Warrior("nexus", 80, hammer)

weapons = [axe, hammer, sword, spear, globes]
warriors = [lancelot, surtr, bercox, navinni, nexus]


def warriors_weapons():
    for warrior in warriors:
        if count == max_counts:
            break
        time.sleep(1)
        print(f"\n[+] The warrior {warrior.name} has the {warrior.weapon.model} weapon with {warrior.weapon.power} power and {warrior.weapon.damage} damage.")
        count += 1
        time.sleep(1)
    return count
        

count = 0
max_counts = 5
  
def warriors_weapons(round_number, counter):
    for warrior in warriors:
            counter += 1
            time.sleep(1)
            print(
                f"\n[{counter}] Round {round_number}: The warrior {warrior.name} has the "
                f"{warrior.weapon.model} weapon with {warrior.weapon.power} power and "
                f"{warrior.weapon.damage} damage."
            )
            time.sleep(1)
    return counter


max_loops = 5

try:
    counter = 0
    for round_number in range(1, max_loops + 1):
        counter = warriors_weapons(round_number, counter)

except KeyboardInterrupt:
    print("\n\n[!] Moving to safe zone ...")