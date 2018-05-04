import numpy as np
import pyglet
import matplotlib.pyplot as plt
width1,height1 = 1024,768
width2,height2 = 1920,1080

f = lambda x,y: 10*x
array1 = np.fromfunction(f,(height1,width1)).astype('uint8')
g = lambda x,y: 10*y
array2 = np.fromfunction(g,(height2,width2)).astype('uint8')



image1 = pyglet.image.ImageData(width1,height1,'L',array1.ravel().tostring())
#display = pyglet.window.get_platform().get_display()
image2 = pyglet.image.ImageData(width2,height2,'L',array2.ravel().tostring())
display = pyglet.canvas.get_display()
screen1 = display.get_screens()[0]
screen2 = display.get_screens()[1]
window1 = pyglet.window.Window(fullscreen=True,screen=screen1)
window2 = pyglet.window.Window(fullscreen=True,screen=screen2)
@window1.event
def on_draw():
    window1.clear()
    image1.blit(0,0)
@window2.event
def on_draw():
    window2.clear()
    image2.blit(0,0)

pyglet.app.run()
