import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x):
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * np.abs(x[0] + 10)  # Bukin function No. 6


def gradient_descent(x, alpha, eta, epochs):
    e = 0
    f_prev = 100
    f_val = 0

    while e < epochs and np.abs(f_prev - f_val) >= eta:
        f_prev = f_val
        df[0] = (0.01 * (x[0] + 10)) / np.abs(x[0] + 10) - (x[0] * (x[1] - 0.01 * x[0] ** 2)) / (np.abs(x[1] - 0.01 * x[0] ** 2)) ** (3 / 2)
        df[1] = (50 * (x[1] - 0.01 * x[0] ** 2)) / np.abs(x[1] - 0.01 * x[0] ** 2) ** (3 / 2)
        x[0] -= alpha * df[0]
        x[1] -= alpha * df[1]

        f_val = f(x)
        e += 1

    return x, f_val


def global_optimum():
    xs = []
    vals = []

    for i in range(-15, 6):
        for j in range(-3, 4):
            x12, value = gradient_descent([i, j], 0.0001, 0.0001, 10000)
            if not np.isnan(value):
                xs.append(x12)
                vals.append(value)

    ind = int(np.argmin(vals))
    return xs[ind], vals[ind]


x1 = np.linspace(-15, 5, 50)
x2 = np.linspace(-3, 3, 50)
df = np.zeros(2)
X, Y = np.meshgrid(x1, x2)
res, val = global_optimum()
print(res, val)

Z = np.zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z)
ax.plot([res[0]], [res[1]], [val], marker='o', markersize=5)
plt.show()
