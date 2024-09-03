import math
 
p1 = (23, -88)
p2 = (6, 42)
 
#tu código va aquí
horiz = p2[0]-p1[0]
vert = p2[1]-p1[1]

horiz = horiz**2
vert = vert**2

p3 = horiz + vert

print(math.sqrt(p3))
