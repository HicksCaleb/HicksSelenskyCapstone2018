import numpy as np
import matplotlib.pyplot as plt
import sys,os
inf = 'out5.tsv'
inFile = open(inf)
data = [1-float(line.split('\t')[1])%1 for line in inFile]
plt.scatter(np.linspace(0,255,256),data)
plt.show()
dF = np.fft.fft(data)
plt.plot(dF)
plt.show()

modDf = dF
modDf[3] = 0
modDf[-3] = 0
outData = np.fft.ifft(modDf)
plt.scatter(np.linspace(0,255,256),outData)
plt.show()

