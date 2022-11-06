a = 0    # global variable

def myfunction(x):    # function to perform simple integration
    global a       #indicates that a global variable is used
    b = ...
    return b


from matplotlib import pyplot as plt   # library needed for plotting

# set plotting parameters
plt.axis([0, 10, 0, 20])      # X axis min,max, Y axis min,max
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (inches)")
plt.grid(True)
plt.figure(figsize=(5,2.5))   # fix for repl.it


velocity = 2        # initial velocity, 2 in/s
distance = 0

for t in range(10):
    plt.scatter(t, distance , s=5, c='r')
    plt.pause(1)

    distance = distance + velocity
