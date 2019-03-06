import numpy as np


def min_value(ar):
    if ar.size == 0:
        print("Given array is empty")
        quit()
    else:
        m = ar[0]
        ind = 0
        for i in range(ar.size):
            if ar[i] < m:
                m = ar[i]
                ind = i
        return m, ind
    # return np.min(ar), np.argmin(ar)


a = np.array([3, 5, 2, 1, 9])
val, index = min_value(a)
print("Minimum number is " + str(val) + ", located at index " + str(index))
