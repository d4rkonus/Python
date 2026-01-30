#!/usr/bin/python3

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
axe = Weapon("Axe", "Ice", 50)
hammer = Weapon("Hammer", "Lightning", 80)
sword = Weapon("Sword", "Fire", 70)
spear = Weapon("Spear", "Air", 40)
globes = Weapon("Globes", "Rock", 45)


# --- Warriors Instances ---
lancelot = Warrior("Lancelot", 70, spear)
surtr = Warrior("Surtr", 90, sword)
bercox = Warrior("Bercox", 60, axe)
navinni = Warrior("Navinni", 50, globes)
nexus = Warrior("Nexus", 80, hammer)


weapons = [axe, hammer, sword, spear, globes]
warriors = [lancelot, surtr, bercox, navinni, nexus]

def warriors_weapons():
    for warrior in warriors:
        print(f"\n[+] The warrior {warrior.name} has a {warrior.weapon.model} weapon with {warrior.weapon.power} power and {warrior.weapon.damage} damage.")

warriors_weapons()