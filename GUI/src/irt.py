import girth as irt
import matplotlib
from numpy.lib.function_base import rot90
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

from jinja2 import Environment, FileSystemLoader

plt.style.use("ggplot")

# file = "../data/sample.csv"



def plot_user(results, df):

    ability = results["Ability"]
    fig, ax = plt.subplots(1, 1)
    ax = np.ravel(ax)

    ax[0].set_title("能力パラメータ推定")
    ax[0].set_ylabel("習熟度", color="b")
    ax[0].tick_params(axis='y', colors='b')
    ax[0].plot(ability, "bo--", lw=0.5)

    ax2 = ax[0].twinx()
    ax2.plot(df.sum(), 'gx--', lw=0.5)
    ax2.set_ylabel("正解数", color="g")
    ax2.tick_params(axis='y', colors='g')

    plt.setp(
        ax[0],
        xticks=np.arange(df.shape[1]),
        xticklabels=[f"対象{str(x).zfill(2)}" for x in range(df.shape[1])],
        )
    ax[0].tick_params('x', labelrotation=90, labelsize=8)
    fig.savefig("../report/user_params.png")

def plot_item(results):
   
    dis = results["Discrimination"]
    diff = results["Difficulty"]

    fig, ax = plt.subplots(1,1)
    ax = np.ravel(ax)
    ax[0].plot(diff, "o--")
    ax[0].set_title("項目パラメータ")
    ax[0].set_ylabel("項目難易度", color="r")
    ax[0].tick_params(axis='y', colors='red')
    plt.setp(ax[0], 
            xticks=[0, 1, 2, 3], 
            xticklabels=[f'項目{x}' for x in range(1, 5)],
            )


    ax3 = ax[0].twinx()
    ax3.tick_params(axis='y', colors='b')
    ax3.set_ylabel("弁別力", color="b")
    ax3.plot(dis, "bo--")

    fig.savefig("../report/item_params.png")

def create_df(df, diff, dis, ability):
    item_dict = {
        "難易度": diff,
        "弁別力": dis
    }

    item_params = pd.DataFrame()
    item_params = item_params.append(pd.DataFrame(item_dict))
    item_params = item_params.rename(index={0: "項目1", 1: "項目2", 2: "項目3", 3: "項目4"})

    item_params = item_params.T


    user_df = df.copy()

    user_df.loc[len(user_df)] = user_df.sum()/4
    user_df.loc[len(user_df)] = ability

    user_df.columns = [f"対象{str(x).zfill(2)}" for x in range(user_df.shape[1])]
    user_df = user_df.rename(index={5: "能力", 4:"正解率"})

    user_df = user_df.T[["正解率", "能力"]]

    return item_params, user_df


def show_html(item_params, user_df, df):
    tmp_df = df.T
    tmp_df.columns = [f"項目{x}" for x in range(1,5)]

    pd.set_option("display.precision", 2)

    env = Environment(loader=FileSystemLoader('../templates'))
    template = env.get_template('report_template.html')

    html = template.render(
        page_title_text='My report',
            title_text='試験結果レポート',
            text ='現代テスト理論を基づいた本試験に対する分析結果。',
            report_summary=tmp_df.describe(),
            item_params=item_params,
            user_params=user_df
            )


    with open("../report/report.html", "w") as f:
        f.write(html)
        


    import webbrowser
    new = 2 # open in a new tab, if possible
    url = r"file://C:\Users\kayeungadrian.tam.mr\Desktop\Project\Random_Scripts\GUI\report\report.html"
    webbrowser.open(url,new=new)


def run_irt(data):
    df = data
   
    results = irt.twopl_mml(df.values)

    dis = results["Discrimination"]
    diff = results["Difficulty"]
    ability = results["Ability"]

    item_params, user_df = create_df(df, diff, dis, ability)

    plot_user(results, df)
    plot_item(results)
    show_html(item_params, user_df, df)
   
# run_irt(pd.read_csv(file))
