from matplotlib import pyplot as plt
import math # needed for math.sin, math.cos
plt.figure(figsize=(5,3.5)) # fix for repl.it plot bug
plt.gca().set_aspect('equal', adjustable='box')

distance_x = 0
distance_y = 0
velocity = 100
a_x = 0
a_y = -9.8
theta = 90
color = ['red', 'blue', 'green', 'yellow', 'orange', 'cyan']

class Velocity_components:
  velocity_x = velocity*math.cos(math.pi*theta/180)
  velocity_y = velocity*math.sin(math.pi*theta/180)
  def change_y (self, a_y):
    self.velocity_y += a_y
    return self.velocity_y
  def change_x (self, a_x):
    self.velocity_x += a_x
    return self.velocity_x

class Reset:
  def reset(self):
    global distance_x
    global distance_y
    global velocity_x
    global velocity_y
    velo.velocity_x = velocity*math.cos(math.pi*theta/180)
    velo.velocity_y = velocity*math.sin(math.pi*theta/180)
    distance_x = 0
    distance_y = 0 

velo = Velocity_components()
reset = Reset()

def change_dy (velocity_y):
  global distance_y
  distance_y = distance_y + velocity_y

def change_dx (velocity_x):
  global distance_x
  distance_x = distance_x + velocity_x

for i in range (0,6,1):
  print("initial x velocity = %2.2f"% velo.velocity_x, "when theta is %2d"% theta, "degrees")
  print("initial y velocity = %2.2f"% velo.velocity_y, "when theta is %2d"% theta, "degrees")
  for t in range (0,100,1):
    plt.scatter(distance_x, distance_y, s=5, c=color[i]) 
    plt.pause(0.01)
    change_dy(velo.change_y(a_y))
    change_dx(velo.change_x(a_x))
    if (distance_y < 0): 
      plt.scatter(distance_x, 0, s=100, c='r')
      plt.pause(0.01)
      break
  theta -= 15
  reset.reset()

