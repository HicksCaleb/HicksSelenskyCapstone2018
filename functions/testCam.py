import numpy as np
import pygame
import pygame.camera

width,height = 640,480

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()

screen = pygame.display.set_mode([width,height])

while 1:
    image = cam.get_image()
    #array = pygame.surfarray.array2d(image)
    array = pygame.surfarray.pixels_red(image)
    array[array<150] =0
    draw = np.stack((array,)*3,axis=2) 
    pygame.surfarray.blit_array(screen,draw)
    #screen.blit(image, (0,0))
    pygame.display.flip()
