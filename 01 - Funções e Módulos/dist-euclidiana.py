import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))
z1 = int(input("z1: "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))
z2 = int(input("z2: "))

p1 = (x1, y1, z1)
p2 = (x2, y2, z2)

distance = math.dist(p1, p2)

print(distance)