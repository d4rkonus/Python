#!/usr/bin/python3

def calc_prefix():
   number = int(input("How may devices do you want to include inside your network? "))

   if number <= 0:
      print("\n[!] Put a number bigger than 0")

   elif number >= 1 and number <= 2:
      print("\n[+] You need a network with a /30 prefix")
      print("\n - Some examples of networks with a /30 prefix are: 192.168.1.0/30, 192.168.1.4/30, 10.10.15.0/30")
   
   elif number >= 3 and number <= 6:
        print("\n[+] You need a network with a /29 prefix")
        print("\n - Some examples of networks with a /29 prefix are: 192.168.15.0/29, 192.168.15.8/29, 10.10.15.0/29")

   elif number >= 7 and number <= 14:
        print("\n[+] You need a network with a /28 prefix")
        print("\n - Some examples of networks with a /28 prefix are: 192.168.15.0/28, 192.168.15.16/28, 10.10.15.0/28")
  
   elif number >= 15 and number <= 30:
        print("\n[+] You need a network with a /27 prefix")
        print("\n - Some examples of networks with a /27 prefix are: 192.168.15.0/27, 192.168.15.32/27, 10.10.15.0/27")

   elif number >= 31 and number <= 62:
        print("\n[+] You need a network with a /26 prefix")
        print("\n - Some examples of networks with a /26 prefix are: 192.168.15.0/26, 192.168.15.64/26, 10.10.15.0/26")
    
   elif number >= 63 and number <= 126:
        print("\n[+] You need a network with a /25 prefix")
        print("\n - Some examples of networks with a /25 prefix are: 192.168.15.0/25, 192.168.15.128/25, 10.10.15.0/25")

   elif number >= 127 and number <= 254:
        print("\n[+] You need a network with a /24 prefix")
        print("\n - Some examples of networks with a /24 prefix are: 192.168.15.0/24, 192.168.15.128/24, 10.10.15.0/24")

   elif number >= 255 and number <= 510:
        print("\n[+] You need a network with a /23 prefix")
        print("\n - Some examples of networks with a /23 prefix are: 192.168.14.0/23, 192.168.16.0/23, 10.10.14.0/23")

   elif number >= 511 and number <= 1022:
        print("\n[+] You need a network with a /22 prefix")
        print("\n - Some examples of networks with a /22 prefix are: 192.168.12.0/22, 192.168.16.0/22, 10.10.12.0/22")
    
   else: 
        print("\n\n[!] Put a number smaller than 1023")


calc_prefix()