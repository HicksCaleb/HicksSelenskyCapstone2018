import numpy as np
import matplotlib.pyplot as plt
import sys, os

#inf = 'out4.tsv'
inf = sys.argv[1]
inFile = open(inf,'r')
y = [float(line.split('\t')[1]) for line in inFile]
#print(type(np.min(y)))
y = y - np.min(y[0])

y = y%1
plt.scatter([x for x in range(len(y))], y)
plt.xlabel("Pixel Value")
plt.ylabel("Wavelength Shift")
plt.title("Calibration of SLM")
plt.show()
