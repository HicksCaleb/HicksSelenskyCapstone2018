import getSlope
import pygame
import pygame.camera
import matplotlib.pyplot as plt
import midpoint
import pyglet
import scipy.interpolate
import numpy as np
width,height = 1024,768
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()

centers = getSlope.initializeCenters(cam)
display = pyglet.canvas.get_display()
screen = display.get_screens()[0]
window = pyglet.window.Window(fullscreen=True,screen=screen)
global image
image = pyglet.image.ImageData(width,height,'L',np.zeros((width,height)).ravel().tostring())

@window.event
def on_draw():
    global image
    window.clear()
    image.blit(0,0)
def update(dT,cam,centers):
    global image
    sX,sY = getSlope.getSlope(cam,centers)
    recon = midpoint.midpoint(sX,sY)
    x = np.arange(0,recon.shape[0])
    y = np.arange(0,recon.shape[1])
    interp = scipy.interpolate.RectBivariateSpline(x,y,recon)
    X = np.linspace(0,recon.shape[0],width)
    Y = np.linspace(0,recon.shape[1],height)
    imageArray = interp(X,Y)
    imageArray = imageArray.transpose()
    imageArray = imageArray-np.min(imageArray)
    imageArray = imageArray/400
    draw = (255*(imageArray)).astype('uint8')
    image = pyglet.image.ImageData(width,height,'L',draw.ravel().tostring())
pyglet.clock.schedule_interval(update,1/120.,cam,centers)
pyglet.app.run()

#while 1:
#    sX,sY = getSlope.getSlope(cam,centers)
#    recon = midpoint.midpoint(sX,sY)
#    plt.clf()
#    plt.subplot(121)
#    plt.imshow(sX,vmin=-20,vmax=20)
#    plt.title("Detected Slopes")
#    plt.subplot(122)
#    plt.imshow(recon)
#    plt.title("Reconstructed Waveform")
#    plt.pause(0.05)
#
