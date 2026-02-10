import sys
import time

def equip_and_progress(weapons, texto="Adding main weapons", delay=0.03):
    # 1️⃣ Mostrar armas
    print("\n[+] Equipping weapons:")
    for weapon in weapons:
        time.sleep(1)
        print(f" · {weapon}")

    # 2️⃣ Progreso del 0 al 100
    for i in range(101):
        sys.stdout.write(f"\r{texto}: {i}% ready")
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(" ⚡ SUPERCHARGED ⚡")
    print()
