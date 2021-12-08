from pynput import keyboard
from time import sleep



s = keyboard.Controller()


print('Press Ctrl-C to quit.')

try:
    while True:

    
        s.press(keyboard.Key.ctrl_l)
        s.release(keyboard.Key.ctrl_l)
        sleep(30)

        

except KeyboardInterrupt:
    print('\n')