from matplotlib import pyplot as plt
import math
plt.gca().set_aspect('equal', adjustable='box')

y=0

#for x in range (0,5,1):
 # y-=1

#  plt.scatter(x, y, s=15, c='b')
  #plt.pause(0.05)

#for x in range (5,9,1):
  #y+=1
  #plt.scatter(x, y, s=15, c='b')
  #plt.pause(0.05)

# prints a complete smiley face with notes, eyes, and a smile!

for x in range (0,9,1):
  y=1/7*(x-4)**2-5
  plt.scatter(x, y, s=15, c='b')
  plt.pause(0.05)

for a in range(0, 360, 10):
  
  y = 7* math.sin(a*math.pi/180)
  x = 7* math.cos(a*math.pi/180)+4

  plt.scatter(x, y, s=15, c='r')
  plt.pause(0.05)

x=1.5
y=2

plt.scatter(x, y, s=100, c='g')
plt.pause(0.05)

x=6.5
plt.scatter(x, y, s=100, c='g')
plt.pause(0.05)

x=4
y=0

plt.scatter(x, y, s=15, c='g')
plt.pause(0.05)

x=4.3
y=-1
plt.scatter(x, y, s=15, c='g')
plt.pause(0.05)

x=3.7
plt.scatter(x, y, s=15, c='g')
plt.pause(0.05)

for x in range(-7,7,1):
  r=7
  y=math.sqrt(r**2-x**2)
  x=x+4
  plt.scatter(x, y, s=15, c='g')
  plt.pause(0.05)

for x in range(-7,7,1):
  r=7
  y=-math.sqrt(r**2-x**2)
  x=x+4
  plt.scatter(x, y, s=15, c='g')
  plt.pause(0.05)

