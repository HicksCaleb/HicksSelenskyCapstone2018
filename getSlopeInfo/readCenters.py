import numpy as np
import pygame
import pygame.camera
from scipy.ndimage.filters import maximum_filter,minimum_filter,gaussian_filter
from scipy.ndimage.morphology import generate_binary_structure,binary_erosion
import matplotlib.pyplot as plt
width,height = 480,480
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()

neighborhood = 37
threshold = 15

image = cam.get_image()
data = pygame.surfarray.pixels_red(image)
#data = gaussian_filter(data,5)
data_max = maximum_filter(data,neighborhood)
maxima = (data==data_max)
data_min = minimum_filter(data,threshold)
diff = ((data_max-data_min) > threshold)
maxima[diff==0] = 0

print(np.sum(maxima))
plt.imshow(maxima)
plt.show()
