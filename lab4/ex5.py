import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x):
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * np.abs(x[0] + 10)  # Bukin function No. 6


def gradient_descent(x, alpha, eta, epochs, prev_init, val_init):
    e = 0
    f_prev = prev_init
    f_val = val_init

    while e < epochs and np.abs(f_prev - f_val) >= eta:
        f_prev = f_val
        df[0] = (0.01 * (x[0] + 10)) / np.abs(x[0] + 10) - (x[0] * (x[1] - 0.01 * x[0] ** 2)) / (np.abs(x[1] - 0.01 * x[0] ** 2)) ** (3 / 2)
        df[1] = (50 * (x[1] - 0.01 * x[0] ** 2)) / np.abs(x[1] - 0.01 * x[0] ** 2) ** (3 / 2)
        x[0] -= alpha * df[0]
        x[1] -= alpha * df[1]

        f_val = f(x)
        e += 1

    return x, f_val


x1 = np.linspace(-15, 5, 50)
x2 = np.linspace(-3, 3, 50)
x_init = [-11.0, 1.0]
prev = f(x_init)
val = 0.0
df = np.zeros(2)
X, Y = np.meshgrid(x1, x2)
x12, value = gradient_descent(x_init, 0.0001, 0.0001, 10000, prev, val)
print(x12, value)

Z = np.zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z)
ax.plot([x12[0]], [x12[1]], [value], marker='o', markersize=5)
plt.show()
