import numpy as np
import pygame.camera
import scipy.interpolate
from scipy.ndimage.filters import maximum_filter,minimum_filter,gaussian_filter
from scipy.ndimage.morphology import generate_binary_structure,binary_erosion
def initializeCenters(camera,centersList = []):
    image = camera.get_image()
    neighborhood = 37
    threshold = 15
    data = pygame.surfarray.pixels_red(image)
    #data = gaussian_filter(data,2)
    data_max = maximum_filter(data,neighborhood)
    maxima = (data==data_max)
    data_min = minimum_filter(data,threshold)
    diff = ((data_max-data_min) > threshold)
    maxima[diff==0] = 0
    for a in range(maxima.shape[0]):
        for b in range(maxima.shape[1]):
            if maxima[a,b] == 1:
                flag = True
                for c in centersList:
                    if ((c.centers[0]-a)**2+(c.centers[1]-b)**2) < 15**2:
                        flag = False
                if flag:
                    centersList.append(center([a,b]))
    print(len(centersList))
    return centersList
def getSlope(camera,centersList,dims=(13,17)):
    image = camera.get_image()
    data = pygame.surfarray.pixels_red(image)
    r = []
    c = []
    sX = []
    sY = []
    cords = []
    for a in centersList:
        r.append(a.centers[0])
        c.append(a.centers[1])
        #cords.append(a.centers)
        f = 5.2/0.003125
        x,y = a.slope(data)
        sX.append(x)
        sY.append(y)
    #SX = scipy.interpolate.interp2d(r,c,sX,kind='linear')
    #SY = scipy.interpolate.interp2d(r,c,sY,kind='linear')
    #SX = scipy.interpolate.CloughTocher2DInterpolator(cords,sX)
    #SY = scipy.interpolate.CloughTocher2DInterpolator(cords,sY)
    SX = scipy.interpolate.Rbf(r,c,sX,function='cubic')
    SY = scipy.interpolate.Rbf(r,c,sY,function='cubic')
    
    
    #R = np.linspace(15,465,dims[0])
    #C = np.linspace(15,625,dims[1])
    R,C = np.meshgrid(np.linspace(15,465,dims[0]),np.linspace(15,625,dims[1]))
    
    slopeX = SX(R,C)
    slopeY = SY(R,C)
    return slopeX,slopeY
#    slopeX = np.zeros(dims)
#    slopeY = np.zeros(dims)
#    l = np.max(image.shape)/np.max(dims)
#    for a in range(dims[0]):
#        for b in range(dims[1]):
#            sX,sY = centerArray[a,b].slope(image,l)
#            slopeX[a,b] = sX
#            slopeY[a,b] = sY
#
class center(object):
    def __init__(self,centers):
        self.centers=centers
    def slope(self,array,length=37,method=0,f = 1):
        array = np.pad(array,int(length/2),"constant",constant_values=0)
        A = array[self.centers[0]:self.centers[0]+length,self.centers[1]:self.centers[1]+length]
        if method == 1:
            cent = (0,0) 
        else:
            cent = np.unravel_index(np.argmax(A),A.shape)
        distX,distY = length/2-cent[0],length/2-cent[1]
        self.sX = (2/3.)*distX/f
        self.sY = (2/3.)*distY/f
        #print(distX)
        #print(distY)
        #print(self.sX)
        #print(self.sY)
        #print(cent)
        #print("")
        return self.sX,self.sY

