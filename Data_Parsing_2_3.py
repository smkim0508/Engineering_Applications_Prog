from statistics import mean
import numpy as np
from matplotlib import pyplot as plt
import math
plt.gca().set_aspect('equal', adjustable='box')

datalist = []
ASCII = "083,117,110,103,109,105,110,075,105,109,"
deliminator = ","

def updatelist(a,b):
  locallist = []
  comb = ""
  for i in range (len(a)):
    char = a[i]
    if char == b:
      locallist.append(int(comb))
      x = 1/4*(i+1)
      y = int(comb)
      plt.scatter(x, y, s=15, c='r')
      plt.pause(0.05)
      comb = ""
    else:
      comb = comb + char
  x = np.array([1,2,3,4,5,6,7,8,9,10])
  y = np.array(locallist)
  m, b = np.polyfit(x, y, 1)
  for x in range (1, len(locallist)+1):
    plt.scatter(x, m*x+b, s=10, c='b')
    plt.pause(0.05)
  return locallist

datalist = updatelist(ASCII, deliminator)

print(datalist)
