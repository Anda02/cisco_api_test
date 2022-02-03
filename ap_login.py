from getpass import getpass

from apfinder import *
from output import *
from netmiko import ConnectHandler

toploop = True
menuloop = True
menu = "0"

print("Please input login credentials.")
username = input("Username: ")
password = getpass("Password: ")

while toploop:
    host = input("AP Name: ")

    wlc = finder(username, password, host)

    cisco_881 = {
        'device_type': 'cisco_ios',
        'host': wlc,
        'username': username,
        'password': password
    }

    ssh = ConnectHandler(**cisco_881)
    ssh.enable()
    menuloop = True
    while menuloop:
        print("\n1. Config Data\n2. 5GHz Radio Data\n3. 2.4 GHz Radio Data\n4. CDP Neighbors\n5. Export Config CSV\n"
              "6. Choose New AP\n7. End Program")
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
        if menu == "5":
            output = ssh.send_command('show ap name ' + host + ' config general')
            print("Exporting CSV...")
            exportcsv(output)
        if menu == "6":
            menuloop = False
        if menu == "7":
            print("Closing program...")
            menuloop = False
            toploop = False
