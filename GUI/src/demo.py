# -*- coding: utf-8 -*-
import PySimpleGUI as sg # PySimpleGUIをインポート
from typing import Optional  # 型推定に用いる
import os

from quiz import quiz

QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'

def kill():
    import wmi

    ti = 0
    
    f = wmi.WMI()

    name = "ssspython.exe"

    for process in f.Win32_Process():     
        print(process.name)
        if process.name == name:
            process.Terminate()
            ti += 1

    if ti == 0:
        print("Process not found!!!")


def check_data(name: str, password: str) -> bool:
    correct_data = ("", "")

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
    ret = None 

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
logo = cv2.imread("assets/aifield.png")
logo = cv2.resize(logo, (200,100))
logo = cv2.cvtColor(logo, cv2.COLOR_RGB2RGBA)
import numpy as np
logo[np.where(np.all(logo[..., :3] == 0, -1))] = 0

imgbytes = cv2.imencode('.png', logo)[1].tobytes()

layout = [
    [sg.Text("ログイン画面", font=('Meiryo UI', 13), size=(20, 2), justification="center")],
    [sg.Text("名前：", size=(10, 1), font=('Meiryo UI', 9)), sg.Input("", size=(25, 1), key="-name-")],
    [sg.Text("パスワード：", size=(10, 1), font=('Meiryo UI', 9)), sg.Input("", size=(25, 1), key="-password-")],
    [sg.Button("ログイン", size=(10, 1), font=('Meiryo UI', 9),enable_events=True, key="-login-"), sg.Button("デモ", size=(10, 1), font=('Meiryo UI', 9), enable_events=True, key="-demo-", button_color="green")],
    [sg.Image(source=imgbytes, key="logo", pad=5)]
]

window = sg.Window("DEMO", layout, size=(450, 450), return_keyboard_events=True, margins=(10, 80),element_justification='center', finalize=True)

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
            sg.popup_auto_close("一致しません。", text_color="red", auto_close_duration=2, no_titlebar=True, keep_on_top=True)
            window["-name-"].update(value="")
            window["-password-"].update(value="")
    
    elif event in ["-demo-"]:
        command = "jupyter nbconvert notebooks/demo.ipynb --to slides --post serve --SlidesExporter.reveal_theme=night --HTMLExporter.theme=dark"
        window.close()
        os.system(command)

window.close()

