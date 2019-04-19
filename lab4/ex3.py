from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def F(x, t):
    dx = [0, 0, 0]  # SIR model
    dx[0] = -b * x[0] * x[1]  # s' = -b * s * i
    dx[1] = b * x[0] * x[1] - k * x[1]  # i' = b * s * i - k * i
    dx[2] = k * x[1]  # r' = k * i
    return dx


k = 1 / 3
b = 1 / 2

x_init = ((100, 1, 0))
t_min = 0
t_max = 10
h = 0.001
t = np.arange(t_min, t_max, h)
x = odeint(F, x_init, t)

p1 = plt.plot(t, x[:, 0])
p2 = plt.plot(t, x[:, 1])
p3 = plt.plot(t, x[:, 2])
plt.title('SIR model')
plt.legend((p1[0], p2[0], p3[0]), ('susceptible', 'infected', 'recovered'))
plt.show()
