from matplotlib import pyplot as plt
import math 

theta = math.pi

for a in range(0, 720, 20):
  v = 169.7 * math.sin(a * math.pi/180)  
  i = 154.3 * math.sin((a * math.pi/180)+theta)  

  plt.scatter(a, v, s=5, c='r')  # plot x,v point with size and color
  plt.scatter(a, i, s=5, c='b')  # plot x,i point with size and color
  plt.pause(0.05)  # delay before next point is plotted