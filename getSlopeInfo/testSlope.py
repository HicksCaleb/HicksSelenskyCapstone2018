import getSlope
import pygame
import pygame.camera
import matplotlib.pyplot as plt
import midpoint
pygame.init()
width,height = 640,960
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()

centers = getSlope.initializeCenters(cam)
#sX,sY = getSlope.getSlope(cam,centers)
#print(sX.shape)
#print(sY.shape)
#plt.imshow(sX)
#plt.show()
#
plt.ion()
while 1:
    sX,sY = getSlope.getSlope(cam,centers)
    recon = midpoint.midpoint(sX,sY)
    plt.clf()
    plt.subplot(121)
    plt.imshow(sX,vmin=-20,vmax=20)
    plt.title("Detected Slopes")
    plt.subplot(122)
    plt.imshow(recon)
    plt.title("Reconstructed Waveform")
    plt.pause(0.05)

