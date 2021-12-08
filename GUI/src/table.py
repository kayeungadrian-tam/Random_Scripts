import PySimpleGUI as sg
import pandas as pd


def table_example():
    df = pd.DataFrame()
    var = df.values.tolist()
    
    table_layout = sg.Table(values=df.T.values.tolist(),
                            headings=[f"問{x}" for x in range(1,5)],
                            # max_col_width=50,
                            def_col_width=5,
                            auto_size_columns=False,
                            justification='center',
                            alternating_row_color='gray',
                            display_row_numbers=True,
                            num_rows=35,
                            key="table")
    return table_layout
