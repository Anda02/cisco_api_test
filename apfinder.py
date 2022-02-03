from output import *
from netmiko import ConnectHandler

wlcname = ['wireless-waz1-wlc-1.ni.infr.ufl.edu', 'wireless-waz1-wlc-2.ni.infr.ufl.edu',
           'wireless-waz2-wlc-1.ni.infr.ufl.edu', 'wireless-waz2-wlc-2.ni.infr.ufl.edu']


def finder(username, password, host):
    loop = 0
    counter = 0
    print("Searching for access point...")
    while loop == 0:
        #print ("Loop counter: " + str(counter))
        # Starts SSH session
        cisco_881 = {
            'device_type': 'cisco_ios',
            'host': wlcname[counter],
            'username': username,
            'password': password
        }
        ssh = ConnectHandler(**cisco_881)
        ssh.enable()
        output = ssh.send_command('show ap name ' + host + ' config general')
        # Checks if AP exists from output
        if "Invalid AP Name" in output:
            counter += 1
        # If it exists stops the loop and returns the WLC string
        else:
            loop = 1
            ssh.disconnect()
            print("AP found on: " + wlcname[counter])
            return wlcname[counter]
