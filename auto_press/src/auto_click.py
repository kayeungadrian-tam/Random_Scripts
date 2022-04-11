from pynput import keyboard
from time import sleep

# from datetime import datetime

# try:
#     while True:
#         now = datetime.now()
#         print(now, end="\r")
# except KeyboardInterrupt:
#     print("\n")
#     print("DONE")
    


s = keyboard.Controller()
print('Press Ctrl-C to quit.')
try:
    while True:
        s.press(keyboard.Key.ctrl_l)
        s.release(keyboard.Key.ctrl_l)
        sleep(30)
except KeyboardInterrupt:
    print('\n')