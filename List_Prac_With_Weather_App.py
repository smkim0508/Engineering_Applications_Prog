from matplotlib import pyplot as plt
import math
plt.gca().set_aspect('equal', adjustable='box')
val = 0

TemperatureF = [30, 31, 39, 27, 41, 44, 48]

for x in range (0, len(TemperatureF)):
  TempF = TemperatureF [x]
  val = val + TempF
  plt.scatter(x, TempF, s=15, c='r')
  plt.pause(0.05)

mean = val/len(TemperatureF)
mean1 = round(mean, 1)
print("Average = %2f"%mean1)

# part 2
# from matplotlib import pyplot as plt
# import math
# plt.gca().set_aspect('equal', adjustable='box')

# TemperatureF = [30, 31, 39, 27, 41, 44, 48]

# for x in range (0, len(TemperatureF)):
#   TempF = TemperatureF [x]
#   plt.scatter(x, TempF, s=15, c='r')
#   plt.pause(0.05)

