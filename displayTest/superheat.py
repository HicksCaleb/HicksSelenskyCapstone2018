import numpy as np
import pyglet
import matplotlib.pyplot as plt
width,height = 1024,768
cf = 2*np.random.rand(5,5)-1+2j*np.random.rand(5,5)-1j
coefficients=np.zeros((height,width),dtype=complex)
coefficients[:5,:5] = cf
#dT = 0.5
c = 50
array = np.fft.fft2(coefficients)
array[:2,:] = 0
array[:,:2] = 0
array[-2:,:] = 0
array[:,-2:] = 0




dArray = np.zeros((height,width))

#display = pyglet.window.get_platform().get_display()
display = pyglet.canvas.get_display()
screen = display.get_screens()[1]

window = pyglet.window.Window(fullscreen=True,screen=screen)
global image

image = pyglet.image.ImageData(width,height,'L',array.ravel().tostring())
print("test") 


@window.event
def on_draw():
    global image 
    window.clear()
    image.blit(0,0)

def diffM(A,axis):
    sl1=()
    sl2=()
    for a in range(len(A.shape)):
        if a == axis:
            sl1 = sl1 + (slice(2,A.shape[a]),)
            sl2 = sl2 + (slice(0,A.shape[a]-2),)
        else:
            sl1 = sl1 + (slice(0,A.shape[a]),)
            sl2 = sl2 + (slice(0,A.shape[a]),)
    return A[sl1]-A[sl2]

def update(dT,array,dArray):
    global image
    laplacian = diffM(diffM(array,0),0)[:,2:-2] + diffM(diffM(array,1),1)[2:-2,:]
    dArray[2:-2,2:-2] = dArray[2:-2,2:-2] + c**2*dT*laplacian
    array = array + dT*dArray

    draw = (128*(array/np.max(array))+127).astype('uint8')
    image = pyglet.image.ImageData(width,height,'L',draw.ravel().tostring())

pyglet.clock.schedule_interval(update,1/120.,array,dArray)
pyglet.app.run()
