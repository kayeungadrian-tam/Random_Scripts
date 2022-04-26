import numpy as np
import matplotlib.pyplot as plt

class PID:
    def __init__(self, P=0.2, I=0.0, D=0.0, deltatime=0.01, windup_guard=20.0):
        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.deltatime=deltatime
        self.windup_guard=windup_guard
        self.reset()

    def reset(self):
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0

    def update(self, feedback_value, target_value):
        error = target_value - feedback_value
        delta_error = error - self.last_error
        self.PTerm = self.Kp * error
        self.ITerm += error * self.deltatime
        self.ITerm = np.clip(self.ITerm, -self.windup_guard, self.windup_guard)

        self.DTerm = delta_error / self.deltatime
        self.last_error = error

        output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)
        return output


if __name__ == '__main__':
    pid = PID(P=0.2, I=0.0,  D=0.0, deltatime=0.01)

    feedbacks = []
    feedback_value = 0.0
    target_value = 1.0
    for i in range(1, 100):
        feedback_value += pid.update(feedback_value, target_value)
        feedbacks.append(feedback_value)

    plt.title('PID control in python')
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.plot(feedbacks, label='target')
    plt.plot([target_value] * 100, label='feedback')
    plt.ylim(-0.2, 1.2)
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()

