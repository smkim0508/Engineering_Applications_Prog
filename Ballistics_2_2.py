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

velocity_x = velocity*math.cos(math.pi*theta/180)
velocity_y = velocity*math.sin(math.pi*theta/180)

def change_vy (a_y):
  global velocity_y
  velocity_y += a_y

def change_vx (a_x):
  global velocity_x
  velocity_x += a_x

def change_dy (velocity_y):
  global distance_y
  distance_y = distance_y + velocity_y

def change_dx (velocity_x):
  global distance_x
  distance_x = distance_x + velocity_x
  
def reset():
  global distance_x
  global distance_y
  global velocity_x
  global velocity_y
  velocity_x = velocity*math.cos(math.pi*theta/180)
  velocity_y = velocity*math.sin(math.pi*theta/180)
  distance_x = 0
  distance_y = 0 

for i in range (0,6,1):
  print("initial x velocity = %2.2f"% velocity_x, "when theta is %2d"% theta, "degrees")
  print("initial y velocity = %2.2f"% velocity_y, "when theta is %2d"% theta, "degrees")
  for t in range (0,100,1):
    plt.scatter(distance_x, distance_y, s=5, c=color[i]) 
    plt.pause(0.01)
    change_vy(a_y)
    change_vx(a_x)
    change_dy(velocity_y)
    change_dx(velocity_x)
    if (distance_y < 0): 
      plt.scatter(distance_x, 0, s=100, c='r')
      plt.pause(0.01)
      break
  theta -= 15
  reset()

