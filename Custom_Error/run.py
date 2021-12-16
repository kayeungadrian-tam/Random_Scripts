#################################
###     ERROR
#################################

class EXPLOSION(Exception):
    def __init__(self):
        with open("messages/explosion.txt", "r", encoding="utf-8") as f:
            explosion = f.read()
        self.message = f"\n\n{explosion}"
        super().__init__(self.message)


class ObamaError(Exception):
    def __init__(self) -> None:
        with open("messages/obama.txt", "r", encoding="utf-8") as f:
            obama = f.read()
        self.message = f"\n\n{obama}"
        super().__init__(self.message)

if False:
    raise EXPLOSION

#################################
###     OTSUKARE
#################################

def otsukare():
    with open("messages/otsukare.txt", "r", encoding="utf-8") as f:
        otsukare = f.read()
    print(otsukare)

# otsukare()

#################################
###     ANIMATED
#################################

import os 
from time import sleep

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def kawaii_goodbye():
    for txt in os.listdir("messages/kawaii"):
        f = open(f"messages/kawaii/{txt}", "r", encoding="utf-8").read()
        sleep(0.2)
        clearConsole()
        print(f)
        

kawaii_goodbye()