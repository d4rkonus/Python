#!/usr/bin/python3

ip = input("\n[+] Give me an IP: ").strip()

for octet in ip.split("."):
    print(f"\n{octet} ---> {format(int(octet), '08b')} ")
