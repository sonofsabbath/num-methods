import numpy as np
import matplotlib.pyplot as plt


def euler(a, h, T):
    initial_x = 1
    t = np.arange(0, T, h)
    x = np.zeros(t.shape)
    try:
        x[0] = initial_x
        for i in range(t.size - 1):
            x[i + 1] = x[i] + h * a * x[i]
    except IndexError:
        print('h and T must be higher than zero')
        quit(-1)
    except TypeError:
        print('a, h, T must be numbers')
        quit(-1)

    h_ideal = 0.00001
    t_ideal = np.arange(0, T, h_ideal)
    x_ideal = np.zeros(t_ideal.shape)
    x_ideal[0] = initial_x

    for i in range(t_ideal.size - 1):
        x_ideal[i + 1] = x_ideal[i] + h_ideal * a * x_ideal[i]

    p1 = plt.plot(t, x)
    p2 = plt.plot(t_ideal, x_ideal)
    plt.title("x' = {}x".format(a))
    plt.xlabel('t')
    plt.ylabel('x')
    plt.legend((p1[0], p2[0]), ('step: {}'.format(h), 'ideal'))
    plt.show()


euler(2, 0.1, 5)
