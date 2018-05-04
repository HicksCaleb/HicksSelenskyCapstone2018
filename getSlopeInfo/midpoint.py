import numpy as np

def midpoint(slopeX,slopeY,v0=0):
    dim = slopeX.shape
    solution = np.zeros(dim)
    solution[0,0] = v0
    for ca,a in enumerate(slopeX[0,1:]):
        solution[0,ca+1] = solution[0,ca]+(slopeX[0,ca]+slopeX[0,ca+1])/2
    for ca,a in enumerate(slopeY[1:,0]):
        solution[ca+1,0] = solution[ca,0]+(slopeY[ca,0]+slopeY[ca+1,0])/2
    for a in range(1,dim[0]):
        for b in range(1,dim[1]):
            avdx = (slopeX[a,b-1]+slopeX[a,b])/2
            wx = 1#np.abs(slopeX[a,b-1])
            xEst = solution[a,b-1]+avdx
            avdy = (slopeY[a-1,b]+slopeY[a,b])/2
            wy = 1#np.abs(slopeY[a-1,b])
            yEst = solution[a-1,b]+avdy
            est = (wy*xEst+wx*yEst)/(wx+wy)
            solution[a,b] = est
    return solution
    
        
        
        
