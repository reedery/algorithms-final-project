import numpy as np

def findCorners(arry, window_size, k, thresh):
    height = len(arry)
    width = len(arry[0])

    dy, dx = np.gradient(arry)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2

    cornerList = []

    offset = window_size/2
    count = 0

    for y in range(offset, height- offset):
        for x in range(offset, width - offset):
            
            windowIxx = Ixx[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIyy = Iyy[y-offset:y+offset+1, x-offset:x+offset+1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            #Find determinant and trace, use to get corner response
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            r = det - k*(trace**2)

            #If corner response is over threshold, color the point and add to corner list
            if r > thresh:
                #print x, y, r
                cornerList.append([y, x, r])
                count +=1
            

    print count
    return cornerList

data = np.loadtxt("/Users/daniellenash/Desktop/AlgsPics/fullRect1.txt")

print findCorners(data, 4, 0.05, 4)




