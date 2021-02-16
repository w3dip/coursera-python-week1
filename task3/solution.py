import sys

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c
square_of_d = D ** 0.5

top1 = b * (-1) + square_of_d
top2 = b * (-1) - square_of_d
bottom = 2 * a

print(int(top1 / bottom))
print(int(top2 / bottom))