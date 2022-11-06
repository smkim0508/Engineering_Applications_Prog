from matplotlib import pyplot as plt
plt.figure(figsize=(5,3.5)) # fix for repl.it plot bug
plt.gca().set_aspect('equal', adjustable='box')

m = 100
Kd = 10
Ks = 80
v = 0
x = 0
x0 = 6
F_sum = 0
a = 0
#Fs = Ks*x0
#Fd = 0
dist = []
dt = []
t = 0

class integrator:
  sum = 0
  def integrate(self, x):
    #self.sum += x
    self.sum += x/5
    return self.sum
  def reset(self):
    self.sum = 0

integrate1 = integrator()
integrate2 = integrator()

for i in range (0, 500):
  #t += 1
  t += 0.2
  Fd = Kd * v
  Fs = -Ks * x
  F_sum = Fd - Fs
  a = -F_sum/m
  v = integrate1.integrate(a)
  x = integrate2.integrate(v)+ x0
  dt.append(t)
  dist.append(x)
  plt.plot(dt, dist, c='r')
  #plt.scatter(t, x, s=5, c='r') 
  plt.pause(0.01)
 




