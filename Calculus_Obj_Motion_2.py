from matplotlib import pyplot as plt

plt.figure(figsize=(5,2.5))
plt.axis([0,10,-50,20])

dist = 0    # global variable
velocity = 6
change_vel = -2

def dist_func(velocity):    # function to perform simple integration
  global dist       #indicates that a global variable is used
  dist += velocity
  return dist
 
class Velo:
  def vel_func(self, change_vel):
    global velocity
    velocity += change_vel
    return velocity

velocity1 = Velo()

for i in range (0,10,1):
  plt.scatter(i, dist, s=30, c='r')
  plt.pause(0.05)

  velocity1.vel_func(change_vel)
  dist_func(velocity)

print("Total Distance: ", dist)
print("Final Velocity: ", velocity)