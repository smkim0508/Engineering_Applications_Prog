from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))   # fix for the bug in repl.it
Vs = 12
Rs = 4

for r in range(1, 31):
  i = Vs/(Rs+r)
  Vl = r*i
  Pl = Vl*i
  
  
  plt.scatter(r, i, s=5, c='r')  # plot current point in red
  plt.scatter(r, Vl, s=5, c='g')  # plot voltage point in green
  plt.scatter(r, Pl, s=5, c='b')

  plt.pause(0.01)  # delay before next point is plotted