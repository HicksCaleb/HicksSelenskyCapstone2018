#My apologies for my poorly written and documented code
#Caleb Hicks
#May 2018
import getSlope
import pygame
import pygame.camera
import matplotlib.pyplot as plt
import midpoint
import pyglet
import scipy.interpolate
import numpy as np
import calcPixels
#set width and height of slm
width,height = 1024,768
#Initialization code for camera
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()
#This is the SLM calibration file
calibFile = open('outFinal.tsv','r')
#Input into memory
calib = [float(line.split('\t')[1]) for line in calibFile]
#so it's easier to work with:
calib = calib-np.min(calib)
y = np.linspace(0,255,256)
#This gives us a function to call to convert wavelengths into pixel values
global f
f = scipy.interpolate.interp1d(calib,y,fill_value="extrapolate")
#Set center locations
centers = getSlope.initializeCenters(cam)
#Set up for displaying to screens
display = pyglet.canvas.get_display()
#screen is our output of the wavefront, slm is the slm screen
screen = display.get_screens()[1]
slm = display.get_screens()[0]
#and make windows on those screens
window = pyglet.window.Window(screen=screen)
winSLM = pyglet.window.Window(fullscreen=True,screen=slm)
global image
global correction
global pastDistortions
global error
error = []
#image is the reconstructed wavefront we display
#Correction is what we display on the SLM
#pastCorrection is the sum of wavefront reconstructions thus far
image = pyglet.image.ImageData(width,height,'L',np.zeros((width,height)).ravel().tostring())
correction = pyglet.image.ImageData(width,height,'L',np.zeros((width,height)).ravel().tostring())
pastDistortions = np.zeros((height,width))
plt.ion()
#Draw the image 
@window.event
def on_draw():
    global image
    window.clear()
    image.blit(0,0)
#Draw the correction
@winSLM.event
def on_draw():
    global correction
    winSLM.clear()
    correction.blit(0,0)
def update(dT,cam,centers):
    global image
    global correction
    global pastDistortions
    global f
    global error
    #slope information
    sX,sY = getSlope.getSlope(cam,centers)
    #A rough estimate of error, which we print and plot
    #e = np.sum(np.abs(sX)+np.abs(sY))


    #Reconstruct the wavefront, and interpolate it out, then get the drawn image
    recon = midpoint.midpoint(sX,sY)
    x = np.arange(0,recon.shape[0])
    y = np.arange(0,recon.shape[1])
    interp = scipy.interpolate.RectBivariateSpline(x,y,recon)
    X = np.linspace(0,recon.shape[0],width)
    Y = np.linspace(0,recon.shape[1],height)
    imageArray = interp(X,Y)
    imageArray = imageArray.transpose()
    imageArray = imageArray-np.min(imageArray)
    drawArray = imageArray
    draw = (255*(drawArray)).astype('uint8')
    image = pyglet.image.ImageData(width,height,'L',draw.ravel().tostring())
    imageArray = imageArray - (np.max(imageArray)-np.min(imageArray))/2
    pastDistortions += imageArray
    

    







    #Convert the wavefront image to the correction image
    unit = (1/2)*(480/14+640/19)*0.003125*10**-3
    distMeters = pastDistortions*unit
    corrWavelengths = 1-(distMeters/(680*10**-9))
    correctionArray=f(corrWavelengths%1)

    #We only see the middle of the SLM, so only draw there
    padArray = np.zeros((768,1024))
    padArray[192:576,256:768] = correctionArray[::2,::2]
    correction = pyglet.image.ImageData(width,height,'L',padArray.astype('uint8').ravel().tostring())
    sigma = (np.mean((2*np.pi*corrWavelengths-np.mean(2*np.pi*corrWavelengths))**2))
    print(np.exp(-sigma))
    print(np.abs(np.mean(np.exp(corrWavelengths*2*np.pi*1j)[:3,:3])))
    e = np.abs(np.mean(np.exp(corrWavelengths*2*np.pi*1j)))**2
    print(e)
    print("")
    plt.ion()
    error.append(e)
    plt.clf()
    plt.plot(error)
    plt.draw()
    plt.pause(0.0001)
    #plt.show()



pyglet.clock.schedule_interval(update,1/120.,cam,centers)
pyglet.app.run()


