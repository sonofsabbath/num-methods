from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def F(x, t):
    dx = [0, 0, 0]
    dx[0] = -x[1] - x[2]
    dx[1] = x[0] + a * x[1]
    dx[2] = b + (x[0] - c) * x[2]
    return dx


a = 0.2
b = 0.2
c = 5.7

x_init = ((1, 1, 1))
t_min = 0
t_max = 10
h = 0.001
t = np.arange(t_min, t_max, h)
x = odeint(F, x_init, t)

plt.plot(t, x)
plt.show()
ax = Axes3D(plt.figure())
ax.plot(x[:, 0], x[:, 1], x[:, 2])
plt.show()
