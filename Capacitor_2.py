from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))   # fix for the bug in repl.it

Vs = 5
R = 10e3    # 10 K
C = 470e-6  # 470 uF
i = 0
Vc = 0 
Tc = 0      # Time Constant (will be determined)
Vr = 0

class integrator:
  total = 0
  def func(self, x):
    self.total += x
    return self.total

integrate_i = integrator()

for t in range(0, 20):
  Vr = Vs - Vc
  i = Vr/R
  Vc = 1/C*integrate_i.func(i)

  if (abs(Vc - 0.63*Vs) < 0.1):
    Tc = t
  plt.scatter(t, Vc, s=5, c='b')
  plt.pause(0.01)  
  plt.scatter(t, i*10000, s=5, c='r')
  plt.pause(0.01)
  

print("Time constant is about", Tc, "s")