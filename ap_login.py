from getpass import getpass
from output import *
from netmiko import ConnectHandler

menuloop = True
menu = "0"
username = input("Username: ")
password = getpass("Password: ")
host = input("AP Name: ")
cisco_881 = {
    'device_type': 'cisco_ios',
    'host': 'wireless-waz2-wlc-1.ni.infr.ufl.edu',
    'username': username,
    'password': password
}

ssh = ConnectHandler(**cisco_881)
ssh.enable()
while menuloop:
    print("\n1. Config Data\n2. 5GHz Radio Data\n3. 2.4 GHz Radio Data\n4. CDP Neighbors\n")
    menu = input("Choose a number from the list above: ")
    if menu == "1":
        output = ssh.send_command('show ap name ' + host + ' config general')
        print("AP Config: ")
        outputconfig(output)
    if menu == "2":
        output = ssh.send_command('show ap name ' + host + ' config dot11 5ghz')
        print("5GHz Radio Data: ")
        outputinfo(output)
    if menu == "3":
        output = ssh.send_command('show ap name ' + host + ' config dot11 24ghz')
        print("2.4GHz Radio Data: ")
        outputinfo(output)
    if menu == "4":
        output = ssh.send_command('show ap name ' + host + ' cdp neighbors')
        print("CDP Neighbors: ")
        print(output)
    menuchange = "y"
    menuchange = input("Choose again? (y/n): ")
    if menuchange == "y":
        menuloop = True
    if menuchange == "n":
        menuloop = False




