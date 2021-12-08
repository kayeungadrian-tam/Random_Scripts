import PySimpleGUI as sg
import cv2
import numpy as np

QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'

def validation(name, password):
    correct_data = ("user", "1234")
    if (name, password) == correct_data:
        return True
    return False

def define_layout(logo):
    layout = [
        [sg.Text("ログイン画面", font=('Meiryo UI', 13), size=(20, 2), justification="center")],
        [sg.Text("名前：", size=(10, 1), font=('Meiryo UI', 9)), sg.Input("", size=(25, 1), key="-name-")],
        [sg.Text("パスワード：", size=(10, 1), font=('Meiryo UI', 9)), sg.Input("", password_char='*', size=(25, 1), key="-password-")],
        [sg.Button("LOGIN", size=(10, 1), font=('Meiryo UI', 9),enable_events=True, key="-login-", button_color="darkblue"), sg.Button("EXIT", size=(10, 1), font=('Meiryo UI', 9), enable_events=True, key="-exit-", button_color="darkred")],
        [sg.Image(source=logo, key="logo", pad=5)]
    ]
    return layout

def define_logo(logo_path):
    logo = cv2.imread(logo_path)
    logo = cv2.resize(logo, (200,100))
    logo = cv2.cvtColor(logo, cv2.COLOR_RGB2RGBA)
    logo[np.where(np.all(logo[..., :3] == 0, -1))] = 0

    imgbytes = cv2.imencode('.png', logo)[1].tobytes()
    
    return imgbytes    

def create_window(title, layout, logo):
    window = sg.Window(title, layout, size=(420, 390), return_keyboard_events=True, margins=(10, 80),element_justification='center', finalize=True)
    window["logo"].update(data=logo)
    return window

def main():
    
    sg.theme("DarkGrey14")
    
    imgbytes = define_logo("./assets/aifield.png")
    layout = define_layout(imgbytes)
    window = create_window("DEMO", layout, imgbytes)

    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, '-exit-', 'Escape:27']:
            break
        
        elif event in ["-login-", '\r', QT_ENTER_KEY1, QT_ENTER_KEY2]:
            if validation(values["-name-"], values["-password-"]):
                window.Hide()
                window["-password-"].update(value="")
                window["-name-"].update(value="")
                sg.popup_no_buttons("Welcome", keep_on_top=True, auto_close=True, auto_close_duration=2)
                window.UnHide()                
            else:
                sg.popup_no_buttons("ERROR: 情報が一致しません。", keep_on_top=True, auto_close=True, auto_close_duration=2, no_titlebar=True, background_color="red")
                window["-password-"].update(value="")

    window.close()

if __name__ == "__main__":
    main()