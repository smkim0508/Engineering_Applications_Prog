from matplotlib import pyplot as plt
import math
plt.gca().set_aspect('equal', adjustable='box')
r=1

for a in range(0, 360, 10):
  
  y = 5* math.sin(a*math.pi/180)
  x =  5* math.cos(a*math.pi/180)

  plt.scatter(x, y, s=15, c='r')
  plt.pause(0.05)


for a in range(0, 360, 10):

  y = 2* math.sin(a*math.pi/180)
  x = 2* math.cos(a*math.pi/180)

  plt.scatter(x, y, s=15, c='r')
  plt.pause(0.05)

