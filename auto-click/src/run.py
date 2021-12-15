from pynput import keyboard
from time import sleep
import PySimpleGUI as sg




import subprocess

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Start'), sg.Button('Stop'),sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)


s = keyboard.Controller()


x = 0
# while x < 500_000_000:
run = False
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        run = False
        break
    
    if event == "Start":
        run = True
        p = subprocess.Popen(r'python C:\Users\kayeungadrian.tam.mr\Desktop\Project\Random_Scripts\auto-click\src\bg.py')
    elif event == "Stop":
        run = False
        p.terminate()
        
        import psutil

        PROCNAME = "python.exe"

        for proc in psutil.process_iter():
            # check whether the process name matches
            print(proc.name)
            if proc.name() == PROCNAME:
                proc.kill()
                pass
        
        
        # keyboard.HotKey( {keyboard.Key.shift, keyboard.KeyCode(char='a')}, on_activate=)
        # with  as f:
        # s.press("c")
        # s.press(keyboard.Key.ctrl_l)
        # s.release("c")
        # s.release(keyboard.Key.ctrl_l)

        
    # if run:            

window.close()