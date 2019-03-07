def min_value(ar):
    if len(ar) == 0:
        print("Given array is empty")
        quit()
    else:
        m = ar[0]
        for i in range(len(ar)):
            if ar[i] < m:
                m = ar[i]

        ind = []
        for i in range(len(ar)):
            if ar[i] == m:
                ind.append(i)
        return m, ind


try:
    n = int(input("How many numbers? "))
except ValueError:
    print("You must enter an integer")
    quit()

a = []
for i in range(n):
    try:
        num = float(input("Enter " + str(i + 1) + ". number: "))
    except ValueError:
        print("You must enter a number (remember to use . instead of ,)")
        quit()
    a.append(num)

val, index = min_value(a)
print("Minimum number is " + str(val) + ", located at index(es) " + str(index))
