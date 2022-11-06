from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))   # fix for the bug in repl.it
Vs = 12
Rs = 4
maxPl = 0
maxRl = 0

for r in range(1, 31):
  i = Vs/(Rs+r)
  Vl = r*i
  Pl = Vl*i
  if (maxPl<Pl):
    maxPl = Pl
    maxRl = r
    AltMethod = (Vl*Vl)/Pl
  
  
  
  plt.scatter(r, i, s=5, c='r')  # plot current point in red
  plt.scatter(r, Vl, s=5, c='g')  # plot voltage point in green
  plt.scatter(r, Pl, s=5, c='b')

  plt.pause(0.01)  # delay before next point is plotted


print("Maximum Load Power = %2d"% maxPl)
print("Load Resistance at Maximum Load Power = %2d"% maxRl)
print("Load Resistance at Maximum Load Power = %2d"% AltMethod)