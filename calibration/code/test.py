import numpy as np
import uc480
import pylab as plt
import time
from uc480_h import *

cam = uc480.uc480()
cam.connect()
img = cam.acquire()
cam.stop()
print(img.shape)
plt.imshow(img)
plt.show()
imFT = np.fft.fft2(img)
#imFT[30:,:-30] = 0.
#imFT[-30:,30:] = 0.
plt.imshow(imFT.real)
plt.show()
im2 = np.fft.ifft2(imFT)
print(im2.shape)
im2 = np.array(im2,dtype = float)
plt.clf()
plt.imshow(im2)
plt.show()



