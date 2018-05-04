import numpy as np
import pygame
import pygame.camera
import matplotlib.pyplot as plt
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()
image = cam.get_image()
array = pygame.surfarray.array2d(image)
print(array.shape)
plt.imshow(array)
plt.show()
