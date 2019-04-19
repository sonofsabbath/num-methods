import scipy as scp
import matplotlib.pyplot as plt
from scipy.optimize import fmin
from mpl_toolkits.mplot3d import Axes3D


def f(x):
    return scp.exp(-x[0] ** 2 - x[1] ** 2)


def neg_f(x):
    return -f(x)


x0 = (0, -2)
x_min = fmin(neg_f, x0)  # minimum of -f(x) = maximum of f(x)

delta = 3
x_knots = scp.linspace(x_min[0] - delta, x_min[0] + delta, 41)
y_knots = scp.linspace(x_min[1] - delta, x_min[1] + delta, 41)
X, Y = scp.meshgrid(x_knots, y_knots)
Z = scp.zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')  # initial point
ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final')  # optimal point
ax.legend()
plt.show()
