from PySimpleGUI.PySimpleGUI import execute_file_explorer
from pynput import keyboard
from time import sleep
import PySimpleGUI as sg
import os

import subprocess



exe_file = "src/auto_click.py"

sg.theme('DarkAmber')

layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2')],
            [sg.Button('Start'), sg.Button('Stop'),sg.Button('Cancel')]]

window = sg.Window('Window Title', layout)


s = keyboard.Controller()


x = 0
# while x < 500_000_000:

run = False

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        run = False
        import psutil

        PROCNAME = "python.exe"

        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()
                pass
        
        break
    
    if event == "Start":
        run = True
        p = subprocess.Popen([f'python {os.path.join(os.getcwd(), exe_file)}'])
    elif event == "Stop":
        run = False
        # try:
        #     p.terminate()
        
        
        # keyboard.HotKey( {keyboard.Key.shift, keyboard.KeyCode(char='a')}, on_activate=)
        # with  as f:
        # s.press("c")
        # s.press(keyboard.Key.ctrl_l)
        # s.release("c")
        # s.release(keyboard.Key.ctrl_l)

        
    # if run:            

window.close()