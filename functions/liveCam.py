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
    screen.blit(image, (0,0))
    pygame.display.flip()
