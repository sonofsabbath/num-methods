import numpy as np
import matplotlib.pyplot as plt

try:
    length = float(input("Enter length of the chart: "))
except ValueError:
    print("Input must be a number (use . except of , if you're entering float)")
    quit()

if length <= 0:
    print("Length of the chart must be higher than zero")
else:
    x = np.linspace(-length / 2, length / 2, 500)
    y = np.sin(x) * np.cos(x ** 2)
    plt.plot(x, y)
    plt.show()
    plt.clf()
