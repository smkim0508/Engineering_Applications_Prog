from matplotlib import pyplot as plt
import math 

PowerFactor = x #some variable
theta = math.acos(PowerFactor)


for a in range(0, 720, 20):
  v = 169.7 * math.sin(a * math.pi/180)  
  i = 154.3 * math.sin((a * math.pi/180)+theta)  

  plt.scatter(a, v, s=5, c='r')  
  plt.scatter(a, i, s=5, c='b')  
  plt.pause(0.05)  