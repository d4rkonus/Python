#!/usr/bin/python3

class CPU:
    def info(self):
        raise NotImplementedError
    

class IntelChip(CPU):
    def info(self):
        return "\n[+] Intel has the following CPU model Chips: Atom, Celeron, Pentium, Core i3, Core i5, Core i7, Core i9, Xeon and ARC."
    
class AMDChip(CPU):
    def info(self):
        return "\n[+] AMD has the following CPU model Chips: Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9, Threadripper and EPYC."
    

class MobileChips(CPU):
    def info(self):
        return "\n[+] Some examples of mobile chips are: Apple M1, Qualcomm Snapdragon 8 Gen 1, Samsung Exynos 2200.\n"    


CPU_list = [
    IntelChip(), 
    AMDChip(),
    MobileChips()
]

def main():
    for cpu in CPU_list:
        print(cpu.info())

if __name__ == "__main__":
    main()