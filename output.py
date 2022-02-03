import os

information = ["Radio Type", "Administrative State", "Number of Supported Power Levels", "Current Tx Power Level",
               "Current Channel", "Channel Width", "Antenna Type", "Antenna Mode", "MIMO"]
infoconfig = ["MAC Address", "AP Serial Number", "IP Address", "Cisco AP Location", "RF Tag Name",
              "Primary Cisco Controller Name", "Primary Cisco Controller IP Address", "AP Mode", "Power Type/Mode",
              "AP Model", "IOS Version", "AP Up Time", "AP CAPWAP Up Time"]

def outputinfo(output):
    for line in output.splitlines():
        tests = line.split(":")
        if tests[0].strip() in information:
            print(line)


def outputconfig(output):
    for line in output.splitlines():
        tests = line.split(":")
        if tests[0].strip() in infoconfig:
            print(line)

def exportcsv(output):
    if os.path.exists("configexport.csv"):
        os.remove("configexport.csv")
    file = open("configexport.csv", "x")
    for line in output.splitlines():
        file = open("configexport.csv", "a")
        file.write(str(str(line).replace("  ", "")).replace(":", ",") + "\n")
        '''
        tests = line.split(":")
        if tests[0].strip() in infoconfig:
            file = open("configexport.csv", "a")
            file.write(str(str(line).replace("  ","")).replace(":",",")+"\n")
        '''