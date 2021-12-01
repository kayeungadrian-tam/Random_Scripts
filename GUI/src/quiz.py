from ctypes import alignment
import PySimpleGUI as sg
import numpy as np
import pandas as pd
from table import table_example


table_layout = table_example()

def quiz():

    col = [f"item{x+1}" for x in range(4)]

    df = pd.DataFrame()
    df.index = col
    placeholder = np.zeros((4))
    correct_answer = ['Q0A2', 'Q1A0', 'Q2A2', 'Q3A2']
    cnt = 0
    ret = None
    q_and_a = [
        ['1. What is the thing that makes light in our solar system',
            ['A. The Moon', 'B. Jupiter', 'C. I dunno', 'D. Who cares']],
        ['2. What is Pluto', ['A. The 9th planet', 'B. A dwarf-planet',
                              'C. The 8th planet', 'D. Goofies pet dog']],
        ['3. When did man step foot on the moon', ['A. 1969', 'B. 1960', 'C. 1970', 'D. 1869']], 
        ['4. What is the name of the author?', ['A. Adrian', 'B. Sasaki', 'C. Minami', 'D. Peter']]
        ]

    # make Header larger
    layout = [[sg.Text('現代テスト理論デモ', font='ANY 15', size=(30, 2))]]

    # "generate" the layout for the window based on the Question and Answer information
    for idx, qa in enumerate(q_and_a):
        q = qa[0]
        a_list = qa[1]
        layout += [[sg.Text(q)]] + [[sg.Radio(a, group_id=q, key=f"Q{idx}A{idx2}")]
                                 for idx2, a in enumerate(a_list)] + [[sg.Text('_' * 50)]]

    layout += [[sg.Button('Submit', key='SUBMIT', button_color="Green"), sg.Button('Random', key='RANDOM', button_color="Blue")]]
    layout += [[sg.Button('EXIT', key='EXIT', button_color="Red")]]

    col1 = layout
    col2 = [
        [sg.Text("データベース", font='ANY 12', size=(20, 1), justification='center')],
        [table_layout]
    ]


    full_layout = [
        [sg.Column(col1), sg.Column(col2)],
    ]


    quiz_window = sg.Window('Multiple Choice Test', full_layout, return_keyboard_events=True)

    while True:  # Event Loop
        event, values = quiz_window.read()
        if event in ('SUBMIT', '\r'):
            data = [k for k, v in values.items() if v==True]
            
            for idx, (x, y) in enumerate(zip(data, correct_answer)):
                if x == y:
                    placeholder[idx] = 1
                else:
                    placeholder[idx] = 0
            
            df[f"try_{str(cnt+1).zfill(2)}"] = placeholder.astype(int)
            
            df.to_csv("../data/sample.csv", index=False)
            quiz_window["table"].update(values=df.T.values.tolist())
            cnt += 1
            
        elif event in (sg.WIN_CLOSED, 'EXIT', "Escape:27"):
            ret = True
            break
        elif event in ['RANDOM', 'r']:
            for u in range(4):
                rn_q = np.random.randint(0, 4)
                quiz_window.Element(f"Q{u}A{rn_q}").Update(value=True)
            
    quiz_window.close()
    return ret
    