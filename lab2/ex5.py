import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_float

n = get_float("Size: ")
if n <= 0:
    print("Size must be higher than zero")
    quit()

x = np.linspace(-n/2 * np.pi, n/2 * np.pi, 500)
y = np.linspace(-n * np.pi, n * np.pi, 500)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.cos(R) ** 2 * np.exp(-0.1 * R)

ax = Axes3D(plt.figure(figsize=(1.5 * n, n)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
plt.show()
