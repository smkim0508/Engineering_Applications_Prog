from matplotlib import pyplot as plt
import math
plt.gca().set_aspect('equal', adjustable='box')
r=1

for a in range(0, 360, 10):
  
  y = r* math.sin(a*math.pi/180)
  x = r* math.cos(a*math.pi/180)
  r+=1

  plt.scatter(x, y, s=15, c='r')
  plt.pause(0.05)

  print("angle =%3d"% a,"   radius =%3d"%r)
  



