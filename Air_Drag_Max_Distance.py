from matplotlib import pyplot as plt
import math # needed for math.sin, math.cos
plt.figure(figsize=(5,3.5)) # fix for repl.it plot bug
plt.gca().set_aspect('equal', adjustable='box')
#F_d = 1/2*p*v^2*C_d*A
p = 1.2
C_d = 0.5
A = 1
mass = 1000 #1000 kg
distance_x = 0
distance_y = 0
velocity = 400
a_x = 0
a_y = -9.8
theta = 0
max_x = 0
opt_angle = 0

class Velocity_components:
  velocity_x = velocity*math.cos(math.pi*theta/180)
  velocity_y = velocity*math.sin(math.pi*theta/180)
  def change_y (self, a_y):
    velo.velocity_y += a_y
    return velo.velocity_y
  def change_x (self, a_x):
    velo.velocity_x += a_x
    return velo.velocity_x

velo = Velocity_components()

class Reset_components:
  def reset(self):
    global distance_x
    global distance_y
    distance_x = 0
    distance_y = 0
    velo.velocity_x = velocity*math.cos(math.pi*theta/180)
    velo.velocity_y = velocity*math.sin(math.pi*theta/180)
reset = Reset_components()

def calculateFD (velocity_x):
  global a_x
  global F_d, p, C_d, A, mass
  F_d = -1/2*p*(velocity_x*velocity_x)*C_d*A
  a_x = F_d/mass
  
def change_dy (velocity_y):
  global distance_y
  global velo
  distance_y = distance_y + velocity_y

def change_dx (velocity_x):
  global distance_x
  global velo
  distance_x = distance_x + velocity_x

for i in range (0,91,1):
  theta = i
  print("x velocity = %2.2f"% velo.velocity_x, "when theta is %2d"% theta, "degrees")
  print("y velocity = %2.2f"% velo.velocity_y, "when theta is %2d"% theta, "degrees")
  for t in range (0,100,1):
    #plt.scatter(distance_x, distance_y, s=5, c='b') 
    #plt.pause(0.01)
    change_dy(velo.change_y(a_y))
    change_dx(velo.change_x(a_x))
    calculateFD(velo.velocity_x)
    #print(velo.velocity_x, a_x)
    if (distance_y < 0): 
      #plt.scatter(distance_x, 0, s=100, c='r')
      #plt.pause(0.01)
     break
  #print(distance_x)
  if distance_x>max_x:
    max_x = distance_x
    #print(max_x)
    opt_angle = theta
  reset.reset()
#print(max_x)

print("Optimal angle is %2d"% opt_angle, "degrees")


