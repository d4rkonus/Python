#!/usr/bin/env python3

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


# --- Weapons ---
axe = Weapon("axe", "ice", 50)
hammer = Weapon("hammer", "lightning", 80)
sword = Weapon("sword", "fire", 70)
spear = Weapon("spear", "air", 40)
globes = Weapon("globes", "rock", 45)

# --- Warriors ---
warriors = [
    Warrior("lancelot", 70, spear),
    Warrior("surtr", 90, sword),
    Warrior("bercox", 60, axe),
    Warrior("navinni", 50, globes),
    Warrior("nexus", 80, hammer),
]


def warriors_weapons(round_number, counter, max_counts):
    for warrior in warriors:
        if counter == max_counts:
            return counter

        counter += 1
        time.sleep(1)
        print(
            f"\n[{counter}] Round {round_number}: "
            f"The warrior {warrior.name} has the "
            f"{warrior.weapon.model} weapon with "
            f"{warrior.weapon.power} power and "
            f"{warrior.weapon.damage} damage."
        )
        time.sleep(1)

    return counter


MAX_ROUNDS = 5
MAX_COUNTS = 5

try:
    counter = 0
    for round_number in range(1, MAX_ROUNDS + 1):
        counter = warriors_weapons(round_number, counter, MAX_COUNTS)
        if counter == MAX_COUNTS:
            break

except KeyboardInterrupt:
    print("\n\n[!] Moving to safe zone ...")
