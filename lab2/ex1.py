import cs50 as cs
import numpy as np

for i in range(2):
    x = cs.get_float("Radius: ")
    if x <= 0:
        print("Radius must be higher than zero")
    else:
        per_x = 2 * np.pi * x
        field_x = np.pi * x ** 2
        print("Perimeter: " + str(per_x) + "   Field: " + str(field_x))
