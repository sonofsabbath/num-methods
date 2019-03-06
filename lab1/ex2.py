try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Factorial of a non-integer can't be calculated")
    quit()

if x < 0:
    print("Factorial of a negative number can't be calculated")
elif x == 0 or x == 1:
    print(str(x) + "! = 1")
else:
    f = 1
    for i in range(2, x + 1):
        f *= i
    print(str(x) + "! = " + str(f))
