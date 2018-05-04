import numpy as np
import pygame
import pygame.camera

width,height = 480,640

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()

screen = pygame.display.set_mode([width,height])



while 1:
    image = cam.get_image()
    #pygame.Surface.blit(image,screen)
    screen.blit(image, (0,0))
    pygame.display.flip()
