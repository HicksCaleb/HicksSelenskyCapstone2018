import numpy
import uc480
import matplotlib.pyplot as plt
cam = uc480.uc480()
cam.connect()
img = cam.acquire()
cam.disconnect()
plt.imshow(img)
plt.show()
