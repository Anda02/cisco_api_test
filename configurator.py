import netmiko

controllernames = ["wireless-waz1-wlc-1", "wireless-waz1-wlc-2", "wireless-waz2-wlc-1", "wireless-waz2-wlc-2", ""]
controllerips = ["10.10.216.40", "10.10.216.43", "10.10.215.40", "10.10.215.43", ""]


def change_ap_name(ssh, apname, ):
    newname = input("Input new AP name (ex. b0001rm0001-1-ap): ")
    output = ssh.send_command("ap name " + apname + " name " + newname)
    print("AP name has been changed to: " + newname)


def change_ap_controller(ssh, apname):
    newcon = input("\n1. wireless-waz1-wlc-1 (10.10.216.40)\n2. wireless-waz1-wlc-2 (10.10.216.43) \n3. "
                   "wireless-waz2-wlc-1 (10.10.215.40)\n4. wireless-waz2-wlc-2 (10.10.215.43)\nSelect the number of "
                   "the controller you want to move the AP to: ")
    ssh.send_command("ap name " + apname + " controller primary " + controllernames[int(newcon) - 1])
    print(apname + " controller will be changed to: " + controllernames[int(newcon) - 1])


def change_ap_rftag(ssh, apname):
    output = ssh.send_command('show ap name ' + apname + " config general | i MAC")
    for line in output.splitlines():
        tests = line.split(":")
        #print(tests[1])
        #print("-------")
        #print(type(tests))
        testsout = tests[1].strip()
        print (testsout.splitlines()[1])
    ssh.disconnect()
