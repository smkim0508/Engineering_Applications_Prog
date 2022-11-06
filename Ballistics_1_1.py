from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))   
distance = 0
v = 2

def integrate_dist (velocity):
  global distance
  for t in range (0,10,1): 
    distance += velocity
    plt.scatter(t, distance, s=5, c='r')
    plt.pause(0.01)

integrate_dist(v)