from matplotlib import pyplot as plt
import math # needed for math.sin, math.cos
plt.figure(figsize=(5,3.5)) # fix for repl.it plot bug
plt.gca().set_aspect('equal', adjustable='box')

distance_x = 0
distance_y = 0
velocity = 100
a_x = 0
a_y = -9.8
theta = 45

class Velocity_components:
  velocity_x = velocity*math.cos(math.pi*theta/180)
  velocity_y = velocity*math.sin(math.pi*theta/180)
  #def change_y (self, a_y):
   # global velo
    #velo.velocity_y += a_y
  

velo = Velocity_components()
print(velo.velocity_x)
print(velo.velocity_y)

def change_y (a_y):
 global velo
 velo.velocity_y += a_y

def change_x (a_x):
 global velo
 velo.velocity_x += a_x

def change_dy (velocity_y):
  global distance_y
  global velo
  distance_y = distance_y + velocity_y

def change_dx (velocity_x):
  global distance_x
  global velo
  distance_x = distance_x + velocity_x

for t in range (0,100,1):
  plt.scatter(distance_x, distance_y, s=5, c='r') 
  plt.pause(0.01)
  change_y(a_y)
  change_dy(velo.velocity_y)
  change_dx(velo.velocity_x)
  if (distance_y + velo.velocity_y < 0): 
    plt.scatter(distance_x, distance_y, s=100, c='r')
    break


#print(velocity*math.cos(math.pi*theta/180))
#print(math.cos(90))
#print(math.cos(90/180))
#print(math.cos(1/2))
#print(math.cos(1/2*math.pi))
#print(math.cos(1/2*math.pi))
#print(math.cos(1.57))
