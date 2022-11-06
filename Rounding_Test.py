import math

x = 10
y = 5

print(x)
print(x, y)
print("x")
print("%x" % x)
print("x = %2d" % x)
print("x = %3d" % x)
print("x =  %3d" % x)
print("x =     %3d" % x)

for x in range(0, 257):
    print("{0:b}".format(x).zfill(8))

for x in range(0, 370, 10):
    print("a = %2d" % x, "sine a = %2d" % math.sin * (a * math.pi / 180))
