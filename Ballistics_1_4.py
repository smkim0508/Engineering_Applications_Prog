from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))   
distance = 0
velocity = 50
a = -9.8

def integrate_dist ():
  max_height = 0
  global distance
  global a
  global velocity
  for t in range (0,100,1): 
    distance += velocity
    if (max_height < distance):
      max_height = distance
    if(distance + velocity <0):
      plt.scatter(t,distance, s=100, c='r') 
      plt.pause(0.01)
      break
    plt.scatter(t, distance, s=5, c='r')
    plt.pause(0.01)
    integrate_velocity(a)
  print("Max Height = %2.2f"% max_height)
    

def integrate_velocity (acceleration):
  global velocity
  velocity += acceleration
integrate_dist()