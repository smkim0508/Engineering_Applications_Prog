from statistics import mean
import numpy as np
from matplotlib import pyplot as plt
import math
plt.gca().set_aspect('equal', adjustable='box')

HighTemp = [48, 42, 37, 25, 40, 42, 43, 40]

def mxb(a):
  for i in range (0, len(a)):
    x = i
    y = a[i]
    plt.scatter(x, y, s=15, c='r')
    plt.pause(0.05)
  x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
  y = np.array(a)
  m, b = np.polyfit(x, y, 1)
  for x in range (0, len(a)):
    plt.scatter(x, m*x+b, s=10, c='b')
    plt.pause(0.05)
  return m, b

slope, y_intercept = mxb(HighTemp)

print("Slope = %2.3f"%slope, "Y-intercept = %2.3f"%y_intercept)

