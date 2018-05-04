import numpy as np
import pyglet
import matplotlib.pyplot as plt
width,height = 1024,768
t=2
cf = 2*np.random.rand(t,t)-1+2j*np.random.rand(t,t)-1j
coefficients=np.zeros((height,width),dtype=complex)
coefficients[:t,:t] = cf

array = np.fft.fft2(coefficients)
array = (128*(array/np.max(array))+127).astype('uint8')
print(array[:5,:5])


f = lambda x,y: 640*y
array = np.fromfunction(f,(height,width)).astype('uint8')




image = pyglet.image.ImageData(width,height,'L',array.ravel().tostring())

#display = pyglet.window.get_platform().get_display()
display = pyglet.canvas.get_display()
screen = display.get_screens()[0]

window = pyglet.window.Window(fullscreen=True,screen=screen)
global n
n=0
@window.event
def on_draw():
    window.clear()
    global n
    n+=1 
    print(n)
    f = lambda x,y: n*y
    array = np.fromfunction(f,(height,width)).astype('uint8')
    
    image = pyglet.image.ImageData(width,height,'L',array.ravel().tostring())
    image.blit(0,0)

pyglet.app.run()
