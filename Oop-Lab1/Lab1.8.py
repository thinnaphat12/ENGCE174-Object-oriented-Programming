#หน้า32
from collections import namedtuple

Point = namedtuple('Poinnt', ['x', 'y'])

p1 = Point(3, 5)
p2 = Point(-1, 2)

print("Coodinates of p1:", p1.x, p1.y)