from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))   
distance = 0
velocity = 50
a = -9.8

def integrate_dist ():
  global distance
  global a
  global velocity
  for t in range (0,100,1): 
    distance += velocity
    if (distance < 0):
      break
    plt.scatter(t, distance, s=5, c='r')
    plt.pause(0.01)
    integrate_velocity(a)
    

def integrate_velocity (acceleration):
  global velocity
  velocity += acceleration

integrate_dist()