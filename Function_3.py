from statistics import mean
import numpy as np

HighTemp = [48, 42, 37, 25, 40, 42, 43, 40]

def mxb(a):
  x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
  y = np.array(a)
  m, b = np.polyfit(x, y, 1)
  return m, b

slope, y_intercept = mxb(HighTemp)

print("Slope = %2.3f"%slope, "Y-intercept = %2.3f"%y_intercept)


