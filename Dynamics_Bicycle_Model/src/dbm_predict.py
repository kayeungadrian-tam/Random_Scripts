import numpy as np

import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout

data = pd.read_csv('../dataset/00_log-2021-03-09.csv', delimiter=',', skiprows=1)
header_column = pd.read_csv('../dataset/00_log-2021-03-09.csv', nrows=1)
header = [name for name in header_column]
data.columns = header

Y = data['delta'].values

columns = [
    'v_x',
    'v_y',
    'Curvature',
]

X = data[columns].values

model = Sequential()

model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

history = model.fit(X, Y, epochs=100, batch_size=10, verbose=100)
model.save('../saved_model/dbm.h5')

plt.plot(history.history["loss"], 'o-', ms=0.5, lw=0.7)
plt.title('model loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid()
plt.show()

_, accuracy = model.evaluate(X, Y)

print(accuracy)

