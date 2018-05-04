import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
def calcPixels(array,calib,wavelength):
    #mask = (1-array)%1
    #pixArray = np.zeros(array.shape)
    #for ca,a in enumerate(calib[:-1]):
    #    pixArray[(mask>a)&(mask<calib[ca+1])]=ca
    #pixArray[array>=calib[-1]]=255
    #return pixArray

    
    cMax = np.max(calib)
    if cMax >= 1:
        dim = array.shape
        y = np.linspace(0,255,256)
        f = interp1d(calib,y,fill_value="extrapolate")
    
        rawMask = (1-array)%1
        scaledMask = f(rawMask/wavelength)%255
        return scaledMask
    else:
        rawMask = (1-array)%1#+(0.5-cMax/2)
        y = np.linspace(0,255,256)
        f = interp1d(calib,y,fill_value='extrapolate')
        scaledMask = f(rawMask/wavelength)
        scaledMask[scaledMask > 255] = 255
        scaledMask[scaledMask < 0] = 0
        return scaledMask
  #      for a in range(dim[0]):
   #     for b in range(dim[1]):
    #        phase = 2*np.pi*array[a,b]/wavelength
     #       for cc,c in enumerate(calib):
      #          if c > phase and c < calib[cc+1]:
       #             pixArray[a,b] = calib[cc]
        #            break
         #   pixArray[a,b] = 255
 #   return pixArray
