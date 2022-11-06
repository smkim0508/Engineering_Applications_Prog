from matplotlib import pyplot as plt 
import math
x = 0 
y = 0
dir = 0

for x in range (0,360, 1):
  if y==0:
    dir = 1
  elif y==10:
    dir = -1

  y+=dir

  plt.scatter(x, y, s=15, c='r')
  plt.pause(0.05)

