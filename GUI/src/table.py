import PySimpleGUI as sg
import pandas as pd



def table_example():
    # try:
        # df = pd.read_csv("../data/sample.csv")
    # except:
    df = pd.DataFrame()
    
    var = df.values.tolist()
    
    print(len(var))
    
    table_layout = sg.Table(values=df.T.values.tolist(),
                            headings=[f"問{x}" for x in range(1,5)],
                            # max_col_width=50,
                            def_col_width=5,
                            auto_size_columns=False,
                            justification='center',
                            alternating_row_color='gray',
                            display_row_numbers=True,
                            num_rows=50,
                            key="table")

    

    # window = sg.Window('Table', layout,size=(400, 400), grab_anywhere=False)
    # event, values = window.read()

    # window.close()

    return table_layout

# table_example()