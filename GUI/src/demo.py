# -*- coding: utf-8 -*-
import PySimpleGUI as sg # PySimpleGUIをインポート
from typing import Optional  # 型推定に用いる


from quiz import quiz

QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'

def check_data(name: str, password: str) -> bool:
    correct_data = ("user", "password")

    if (name, password) == correct_data:
        return True
    return False

def display_main() -> Optional[bool]:

    main_layout = [
        [sg.Text("メイン画面")],
        [sg.Text("ようこそ メイン画面へ")],
        [sg.Button("ログアウト", size=(10, 1), enable_events=True, key="-logout-")]
    ]

    main_window = sg.Window("メイン画面", main_layout, size=(400, 400))
    ret = None # 返り値

    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        elif event == "-logout-":
            logout_ret = sg.PopupOKCancel("ログアウトしますか？", title="ログアウト確認", keep_on_top=True)

            if logout_ret == "OK":
                ret = True
                break
            else:
                continue

    main_window.close()
    return ret


sg.theme("DarkGrey14")

import cv2
logo = cv2.imread("../assets/aifield.png")
logo = cv2.resize(logo, (200,100))
logo = cv2.cvtColor(logo, cv2.COLOR_RGB2RGBA)
import numpy as np
logo[np.where(np.all(logo[..., :3] == 0, -1))] = 0

imgbytes = cv2.imencode('.png', logo)[1].tobytes()

layout = [
    [sg.Text("ログイン画面", font=('Meiryo UI', 13), size=(20, 2), justification="center")],
    [sg.Text("名前：", size=(10, 1), font=('Meiryo UI', 9)), sg.Input("", size=(25, 1), key="-name-")],
    [sg.Text("パスワード：", size=(10, 1), font=('Meiryo UI', 9)), sg.Input("", size=(25, 1), key="-password-")],
    [sg.Button("ログイン", size=(10, 1), font=('Meiryo UI', 9),enable_events=True, key="-login-")],
    [sg.Image(source=imgbytes, key="logo", pad=10)]
]

window = sg.Window("DEMO", layout, size=(400, 400), return_keyboard_events=True, margins=(10, 80),element_justification='center', finalize=True)

window["logo"].update(data=cv2.imencode('.png', logo)[1].tobytes())

while True:
    event, values = window.read()

    if event in [sg.WIN_CLOSED, 'Exit', 'Escape:27']:
        break
    
    elif event in ["-login-", '\r', QT_ENTER_KEY1, QT_ENTER_KEY2]:
        if check_data(name=values["-name-"], password=values["-password-"]):
            window["-name-"].update(value="")
            window["-password-"].update(value="")
            window.Hide()
            main_return = quiz()
            if main_return is None:
                break
            window.UnHide()
        else:
            sg.popup_ok("一致しません。")
            window["-name-"].update(value="")
            window["-password-"].update(value="")
window.close()