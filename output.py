information = ["Radio Type", "Administrative State", "Number of Supported Power Levels", "Current Tx Power Level",
               "Current Channel", "Channel Width", "Antenna Type", "Antenna Mode", "MIMO"]
infoconfig = ["MAC Address", "AP Serial Number", "IP Address", "Cisco AP Location", "RF Tag Name",
              "Primary Cisco Controller Name", "Primary Cisco Controller IP Address", "AP Mode", "Power Type/Mode",
              "AP Model", "IOS Version", "AP Up Time", "AP CAPWAP Up Time"]

'''
def outputinfo(output):
    counter = 0
    while counter < len(information):
        for line in output.splitlines():
            if information[counter] in line:
                print(line)
        counter += 1
'''
def outputinfo(output):
    for line in output.splitlines():
        tests = line.split(":")
        if tests[0].strip() in information:
            print(line)

'''
def outputconfig(output):
    counter = 0
    while counter < len(infoconfig):
        for line in output.splitlines():
            if infoconfig[counter] in line:
                print(line)
        counter += 1
'''

def outputconfig(output):
    for line in output.splitlines():
        tests = line.split(":")
        if tests[0].strip() in infoconfig:
            print(line)