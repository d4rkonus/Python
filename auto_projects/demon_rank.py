#!/usr/bin/python3

class Demon:
    def __init__(self, name, rank,  domain, power):
        self.name = name
        self.rank = rank
        self.domain = domain
        self.power = power


    def present(self):
        return (
            f"\n[+] The demon {self.name}"
            f"\n    Rank: {self.rank}"
            f"\n    Domain: {self.domain}"
            f"\n    Power: {self.power}"
        )

class Emperor(Demon):
     def present_emp(self):
        return (
            f"\n[+] Emperor: {self.name}"
            f"\n    Rank: {self.rank}"
            f"\n    Domain: {self.domain}"
            f"\n    Power: {self.power}"
        )

class General(Demon):
    def present_gen(self):
        return (
            f"\n[+] General: {self.name}"
            f"\n    Rank: {self.rank}"
            f"\n    Domain: {self.domain}"
            f"\n    Power: {self.power}"
        )


class Prince(Demon):
    def present_pri(self):
        return (
            f"\n[+] Prince: {self.name}"
            f"\n    Rank: {self.rank}"
            f"\n    Domain: {self.domain}"
            f"\n    Power: {self.power}"
        )
    

class Duque(Demon):
     def present_gen(self):
        return (
            f"\n[+] Duque: {self.name}"
            f"\n    Rank: {self.rank}"
            f"\n    Domain: {self.domain}"
            f"\n    Power: {self.power}"
        )
    

class Guardian(Demon):
    def present_gua(self):
        return (
            f"\n[+] Guardian: {self.name}"
            f"\n    Rank: {self.rank}"
            f"\n    Domain: {self.domain}"
            f"\n    Power: {self.power}"
        )
    

minos = Guardian("Minos", "Guardian", "Entry to the hell", "judgement")
asmodeus = Prince("Asmodeus","Prince", "2 circle of the hell", "lust")
cerberus = Guardian("Cerberus", "Guardian", "3 circle of the hell", "gluttony")
belcebu = Guardian("Belcebu", "Guardian", "3 circle of the hell", "greed")
mammon = Guardian("Mammon", "Guardian", "4 circle of the hell", "greed")
plutto = Guardian("Plutto", "Guardian", "4 circle of the hell", "greed")
satan = General("Satan","General", "5 circle of the hell", "betrayal")
furies = General("Furies","General", "6 circle of the hell", "violence")
minotaur = General("Minotaur","General", "7 circle of the hell", "violence")
paimon = General("Paimon","General", "8 circle of the hell", "fraud")
lucifer = Emperor("Lucifer","Absolute emperor", "9 circle of the hell", "betrayal")


print(lucifer.present())
print(paimon.present())
print(minotaur.present())
print(furies.present())
print(satan.present())
print(plutto.present())
print(mammon.present())
print(belcebu.present())
print(cerberus.present())
print(asmodeus.present())
print(minos.present())
