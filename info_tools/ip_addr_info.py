#!/usr/bin/python3

import ipaddress

def check_network(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)

        mask = network.netmask
        id = network.network_address
        broadcast = network.broadcast_address
        total_hosts = network.num_addresses - 2 if network.prefixlen < 31 else network.num_addresses # Si se añaden las 2 primeras IPs, se pueden restar. Pero si no hay rango, no

        print(f"\n[+] Network analized --> {network}")
        print(f"[+] Network mask --> {mask}")
        print(f"[+] Broadcast address --> {broadcast}")
        print(f"[+] Total hosts available --> {total_hosts}")

        if network.prefixlen < 31:
            host = list(network.hosts())
            print(f"\n[+] First host available --> {host[0]}")
            print(f"\n[+] Last host available --> {host[-1]}\n")

    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\n[!] Moving to safe zone...")

cidr_input = input("Give me an IP and prefix (ex: 192.168.1.10/26): ") 
check_network(cidr_input)