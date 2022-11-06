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
theta = 45

class Integrator:
  total = 0
  def change(self, x):
    self.total += x
    return self.total

integrate_vx = Integrator()
integrate_vy = Integrator()
integrate_dx = Integrator()
integrate_dy = Integrator()

velocity_x0 = velocity*math.cos(math.pi*theta/180)
velocity_y0 = velocity*math.sin(math.pi*theta/180)
velocity_x = velocity_x0
velocity_y = velocity_y0

print("x velocity = %2.2f"% velocity_x0, "when theta is %2d"% theta, "degrees")
print("y velocity = %2.2f"% velocity_y0, "when theta is %2d"% theta, "degrees")

#print(velocity_y0)

for t in range (0,100,1):
  plt.scatter(distance_x, distance_y, s=5, c='b') 
  plt.pause(0.01)
  velocity_x = integrate_vx.change(a_x) + velocity_x0
  velocity_y = integrate_vy.change(a_y) + velocity_y0
  #print("vel x =", velocity_x)
  #print("vel y =", velocity_y)
  distance_x = integrate_dx.change(velocity_x) 
  distance_y = integrate_dy.change(velocity_y)
  F_d = -1/2*p*(velocity_x*velocity_x)*C_d*A
  a_x = F_d/mass  
  #print(velo.velocity_x, a_x)
  if (distance_y < 0): 
    plt.scatter(distance_x, 0, s=100, c='r')
    plt.pause(0.01)
    break
print(distance_x)

