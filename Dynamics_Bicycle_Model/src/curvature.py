import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

from dynamic_bicycle_model import Course, Vehicle, PID


bike = Vehicle(
    x = 0,
    y = 10,
    v = 30,
    yaw = 0,
    yaw_rate = 0.,
    beta = 0.0
)

pid = PID(P=1)
feedback = 0.05

t, X, Y, C = [], [], [], []

for i in range(5000):


    bike.update(delta=feedback)
    target = bike.predict()
    feedback += pid.update(feedback, target)
    t.append(i)
    X.append(bike.x)
    Y.append(bike.y)
    C.append(bike.curve)

    # print(bike.curve)

fig = plt.figure(figsize=(10,7))
for idx, v in enumerate([X, Y, C]):
    ax = fig.add_subplot(311+idx)
    ax.grid()
    if idx == 0:
        ax.set_title('X 座標')
        ax.set_ylabel('[m]')
    elif idx == 1:
        ax.set_title('Y 座標')
        ax.set_ylabel('[m]')
    else:
        ax.set_title('曲率')
        ax.set_ylabel('[1/m]')
        ax.set_xlabel('走行時間 [step]')
        ax.axhline(y=0.004, c='r',label='Real Curvature')
        ax.legend()
    ax.plot(t,v)
plt.tight_layout()
plt.show()




print('Done')