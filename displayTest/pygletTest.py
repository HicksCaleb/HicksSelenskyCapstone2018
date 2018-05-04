import numpy as np
import pyglet
import matplotlib.pyplot as plt
width,height = 1024,768
array = np.zeros((height,width)).astype('uint8')
array[int(height/2):,:] = 255
image = pyglet.image.ImageData(width,height,'L',array.ravel().tostring())
#display = pyglet.window.get_platform().get_display()
display = pyglet.canvas.get_display()
screen = display.get_screens()[1]

window = pyglet.window.Window(fullscreen=True,screen=screen)

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)

pyglet.app.run()
