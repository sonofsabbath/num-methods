import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x):
    return np.cos(x[0] + x[1]) * np.sin(x[0] - x[1])


def derivative(x):
    df = np.zeros(2)
    df[0] = np.cos(x[0] - x[1]) * np.cos(x[0] + x[1]) - np.sin(x[0] - x[1]) * np.sin(x[0] + x[1])
    df[1] = - np.sin(x[0] - x[1]) * np.sin(x[0] + x[1]) - np.cos(x[0] - x[1]) * np.cos(x[0] + x[1])
    return df


def gradient_descent(x, alpha, eta, epochs):
    f_val = f(x)
    f_prev = f_val * 10000
    e = 0

    while e < epochs and np.abs(f_prev - f_val) >= eta:
        f_prev = f_val
        grad = derivative(x)
        x[0] -= alpha * grad[0]
        x[1] -= alpha * grad[1]

        f_val = f(x)
        e += 1

    return x, f_val


def global_optimum(tries, alpha, eta, epochs, geta):
    x12 = []
    vals = []
    found_global = 0
    success = 0
    total = 0

    for i in range(tries):
        x_init = np.random.randn(2)
        xx, nval = gradient_descent(x_init, alpha, eta, epochs)
        print('Attempt {}:'.format(i+1))

        if not np.isnan(nval):
            x12.append(xx)
            vals.append(nval)
            print('x1: {}, x2: {}, value = {}'.format(xx[0], xx[1], nval))

            if 1 + nval <= geta:
                found_global += 1
            success += 1
        else:
            print('Failed to compute local optimum')

        total += 1

    imin = int(np.argmin(vals))
    optx = x12[imin]
    optval = vals[imin]
    print('\nGlobal minimum is {}, found at {}'.format(optval, optx))
    print('Probability of finding value close to global optimum: {}%'.format((found_global / total) * 100))
    print('Success / total optimization trials rate: {}%'.format((success / total) * 100))

    return optx, optval


attempts = 1000
l_rate = 0.01
prec = 0.00001
max_epochs = 10000
glob_prec = 0.001
xy, z = global_optimum(attempts, l_rate, prec, max_epochs, glob_prec)

x1 = np.linspace(-2 * np.pi, 2 * np.pi, 500)
x2 = np.linspace(-2 * np.pi, 2 * np.pi, 500)
X, Y = np.meshgrid(x1, x2)
Z = np.cos(X + Y) * np.sin(X - Y)

ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z)
ax.plot([xy[0]], [xy[1]], [z], markersize=5, marker='o', color='red')
plt.show()
