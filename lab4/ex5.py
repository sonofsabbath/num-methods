import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x):
    return -np.abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(np.abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi)))


x1 = np.linspace(-10, 10, 40)
x2 = np.linspace(-10, 10, 40)
X, Y = np.meshgrid(x1, x2)

Z = np.zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z)
plt.show()
