import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import yaml
import japanize_matplotlib

from openpyxl import Workbook
import openpyxl
import pandas as pd
import string



import os
import os.path
from os import path



import datetime
from tqdm import tqdm

with open('config.yaml') as file:
    params = yaml.load(file, Loader=yaml.FullLoader)

    dt =    params['dt']
    l =     params['l']
    lf =    params['lf']   
    lr = l - lf

    Cf =    params['Cf']
    Cr =    params['Cr']
    Iz =    params['Iz']
    m =     params['m']

    tp =    params['tp']

    A = (-m*(lf*Cf - lr*Cr))/(2*(l**2)*Cr*Cf)

fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')

fig2 = plt.figure(figsize=(14,8))
fig2.suptitle('結果一覧')


ax.set_xlabel('車速 [km/h]')
ax.set_ylabel('走行時間 [s]')
ax.set_zlabel('タイヤ角 [rad]')

ax.set_title('NN推論結果の理想値の比較')

ax.set_xlim(90,50)

entries = os.listdir('../data/')

vector_to_plot = []
velocity = []
delta_to_plot = []
R_list = [300,200,100,50]

for idx, dir_1 in enumerate(entries):
    data = pd.read_csv(f'../data/{dir_1}/NN/00_log-2021-03-19.csv',encoding="SHIFT-JIS", delimiter=',', skiprows=1)
    header_column = pd.read_csv(f'../data/{dir_1}/NN/00_log-2021-03-19.csv',encoding="SHIFT-JIS", nrows=1)
    header = [name for name in header_column]
    data.columns = header
    
    prediction = data['NN推論'].values


    delta = data['タイヤ角'].values

    vector_to_plot.append((list(prediction)))

    velocity.append(dir_1)

    delta_to_plot.append(list(delta))


ts = np.arange(0,80,0.01)



v_list = [50+5*u for u in range(0,9)]



for idx, v in enumerate(v_list):
    real_radians = np.zeros((4,1))
    v1 = v/3.6
    real_radians[0] = (1-((m*(Cf*lf - Cr*lr))*v1**2/(2*l**2*Cf*Cr)))*(l/300)*(1.7)
    real_radians[1] = (1-((m*(Cf*lf - Cr*lr))*v1**2/(2*l**2*Cf*Cr)))*(l/200)*(1.7)
    real_radians[2] = (1-((m*(Cf*lf - Cr*lr))*v1**2/(2*l**2*Cf*Cr)))*(l/100)*(1.7)
    real_radians[3] = (1-((m*(Cf*lf - Cr*lr))*v1**2/(2*l**2*Cf*Cr)))*(l/50)*(1.7)

    ax.plot([v]*len(vector_to_plot[idx]),ts[:len(vector_to_plot[idx])],vector_to_plot[idx], c=f'C{idx}')

    ax2 = fig2.add_subplot(331+idx)
    ax2.set_title(f'車速: {v} km/h')
    ax2.set_ylabel('[rad]')
    ax2.set_xlabel('time [s]')
    ax2.plot(ts[:len(vector_to_plot[idx])],delta_to_plot[idx], c='b', label='タイヤ角')
    ax2.plot(ts[:len(vector_to_plot[idx])],vector_to_plot[idx], c='r', label='NN')

    for k in range(0,4):
        ax.plot([v]*len(vector_to_plot[idx]),ts[:len(vector_to_plot[idx])],real_radians[k], c=f'C{idx}', lw=1, alpha=0.7, ls='dashed')

        if k != 3:
            ax2.axhline(y=real_radians[k], c='k', ls='dashed', lw=0.8)
        else:
            ax2.axhline(y=real_radians[k], c='k', ls='dashed', lw=0.8, label='理想値')
    ax2.legend(fontsize=6, loc='upper left')


plt.tight_layout()
plt.show()