# a = 1, b = 4, c = 3
import math
a = (int(input("Enter a:")))
b = (int(input("Enter b:")))
c = (int(input("Enter c:")))

d = b * b - 4 * a * c
if d < 0:
    print("result is NIL")
else:
    sq1 = (-b + math.sqrt(d))/2*a
    sq2 = (-b - math.sqrt(d))/2*a
    print("First result is: %d" %sq1)
    print("Second result is: %d" %sq2)
