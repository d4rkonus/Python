#!/usr/bin/python3

class Animal:
    def info(self):
        raise NotImplementedError
    

class Carnivoro(Animal):
    def info(self):
        return "\n[+] El carnívoro vivo más grande es la Ballena azul, tiene un peso de 150.000 kg."
    

class Herbivoro(Animal):
    def info(self):
        return "\n[+] El herbívoro vivo más grande es el Elefante africano, tiene un peso de 6.000 kg."

class Carroñero(Animal):
    def info(self):
        return "\n[+] El carroñero vivo más grande es el Cóndor andino, tiene un peso de 15 kg.\n"
    

animales = [
    Carnivoro(),
    Herbivoro(),
    Carroñero()
]

for animal in animales:
    print(animal.info())