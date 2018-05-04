import numpy as np
import matplotlib.pyplot as plt
import sys, os

inf = sys.argv[1]
inFile = open(inf,'r')
y = [float(line.split('\t')[1]) for line in inFile]
y = y - np.min(y[0])

y = y%1

a = np.polyfit(np.linspace(0,255,256),y,2)

z = [a[0]*x**2+a[1]*x+a[0] for x in range(255)]

#z = [a[0]*x+a[1] for x in range(256)]

plt.scatter([x for x in range(len(y))], y)
plt.plot(z)
plt.show()
