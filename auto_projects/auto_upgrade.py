#!/usr/bin/python3
import subprocess
import os
import re

def check_root():
    uid = os.getuid()
    if uid != 0:
        print("\n[!] Run this file as root.")
        exit(1)

def number_of_packages():
    # Check the numnber of packages to be upgraded
    update = subprocess.run( # execute the command "apt-get update" on the system
        ["apt-get", "update"],
        stdout=subprocess.DEVNULL, # hide the output of the command
        stderr=subprocess.DEVNULL, # hide the error output of the command
        )
    
    if update.returncode != 0:
        raise RuntimeError("[!] Something failed.")
    
    # Simulate the upgrading to see which pachages will be upgraded
    result = subprocess.run(
        ["apt-get", "-s", "upgrade"], 
        capture_output=True, # capture the output of the command on binary format
        text=True # becomes the binary output into a text string format
    )

    match = re.search(r"(\d+) upgraded, ", result.stdout)

    if match:
        return int(match.group(1))
    
    return 0


def main():
    check_root()

    upgrades = number_of_packages()

    if upgrades > 0:
        print(f"\n[+] There are {upgrades} packages to be upgraded.")
        print("\n[+] Upgrading the system...")
        subprocess.run(["apt-get", "upgrade", "-y"])
        print("\n[+] System upgraded successfully.")
    else:
        print("\n[+] No need to upgrade the system.")

if __name__ == "__main__":
    main()