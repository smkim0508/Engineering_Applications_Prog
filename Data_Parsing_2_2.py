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
      locallist.append(comb)
      x = 1/4*(i+1)
      y = int(comb)
      plt.scatter(x, y, s=15, c='r')
      plt.pause(0.05)
      comb = ""
    else:
      comb = comb + char
  return locallist

datalist = updatelist(ASCII, deliminator)

print(datalist)

