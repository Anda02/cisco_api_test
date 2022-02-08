from getpass import getpass

from apfinder import *
from output import *
from configurator import *
from netmiko import ConnectHandler

toploop = True
showmenuloop = False
configmenuloop = False
menu = "0"
# Commands to be inserted into SSH
commands = [" config general", ' config dot11 5ghz', ' config dot11 24ghz', ' cdp neighbors', ' config general', "", ""]
# Console description for commands.
commandsprint = ["AP Config: ", "5GHz Radio Data: ", "2.4GHz Radio Data: ", "CDP Neighbors: ", "Exporting CSV...", "",
                 ""]

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
    menu2 = input("\n1. Config AP\n2. AP Info\nChoose a number from the list above: ")
    if menu2 == "1":
        configmenuloop = True
        showmenuloop = False
    if menu2 == "2":
        configmenuloop = False
        showmenuloop = True
    while configmenuloop:
        configmenu = input("\n1. Change AP Name\n2. Change AP Controller\n3. Change RF Tag\nChoose a number from the "
                           "list above: ")
        if configmenu == "1":
            change_ap_name(ssh, host)
            configmenuloop = False
        if configmenu == "2":
            change_ap_controller(ssh, host)
            configmenuloop = False
        if configmenu == "3":
            change_ap_rftag(ssh, host)
            configmenuloop = False

    while showmenuloop:
        print("\n1. Config Data\n2. 5GHz Radio Data\n3. 2.4 GHz Radio Data\n4. CDP Neighbors\n5. Export Config CSV\n"
              "6. Choose New AP\n7. End Program")
        menu = input("Choose a number from the list above: ")
        output = ssh.send_command('show ap name ' + host + commands[int(menu) - 1])
        print(commandsprint[int(menu) - 1])
        if menu == "1":
            outputconfig(output)
        if menu == "2" or menu == "3":
            outputinfo(output)
        if menu == "4":
            print(output)
        if menu == "5":
            exportcsv(output)
        if menu == "6":
            showmenuloop = False
        if menu == "7":
            print("Closing program...")
            showmenuloop = False
            toploop = False
