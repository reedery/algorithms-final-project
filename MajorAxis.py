import numpy as np
import random
import math
from scipy import ndimage
#data = np.loadtxt("/Users/daniellenash/Desktop/algorithms-final-project/triangles/tri4.txt")

#x, y  = np.shape(data)

#x, y = 64, 64

#X, Y = 8, 10
#sums = []

global X
global Y
global sum
global coord
global data

data = np.loadtxt("/Users/daniellenash/Desktop/algorithms-final-project/triangles/tri2.txt")

#x, y  = np.shape(data)

X, Y = np.shape(data)
sum = 0
coord = [(0, 0), (X, Y)]


def majorAxis():
    #numAxis = random.randint(5, 25)
    numAxis = 20
    doX = True
    x1, x2, y1, y2 = 0, 0, 0, 0
    
    thisSum = 0 
    sum = 0
    
    for i in range(numAxis):
        if doX == True:
            x1 = random.randint(0, X)
            x2 = random.randint(0, X)
            y1 = 0
            y2 = Y
            doX = False
            x1 = min(x1, x2)
            x2 = max(x1, x2)
        else:
            y1 = random.randint(0, Y)
            y2 = random.randint(0, Y)
            x1 = 0
            x2 = X
            doX = True
            y1 = min(y1, y2)
            y2 = max(y1, y2)
        
        thisSum = plotLine(x1, x2, y1, y2)
        
        if thisSum > sum:
            sum = thisSum
            coord = [(x1, y1), (x2, y2)]
            
    
    return sum, coord
        


def plotLine(x1, x2, y1, y2):
    currSum = 0    
    dx = x2 - x1
    dy = y2 - y1
    
    dy2 = 2 * (dy)
    dx2 = 2 * dx
    minus = dy2 - 2 * dx
    p = dy2 - dx
   
   
    if dx > dy:
        frac = dy2 - dx
        
        while x1 != x2:
            x1 +=1
            
            if frac >= 0:
                y1 +=1
                frac  -=dx2
            
            frac += dy2
            
            if ((0 <=x1) and (x1 < X) and (0 <= y1) and (y1 < Y)):
                currSum += data[x1][y1]
    else:
        frac = dx2 - dy
        
        while y1 != y2:
            y1 +=1
            
            if frac >= 0:
                x1 +=1
                frac  -= dy2
            
            frac += dx2
            
            if ((0 <=x1) and (x1 < X) and (0 <= y1) and (y1 < Y)):
                currSum += data[x1][y1]
                
                
    return currSum
    

#X, Y = 8, 10

sum, coord = majorAxis()
print sum, coord


def findAngle(coord):
    if coord[1][0] - coord[0][0] == 0:
        return 90
    m = (1.0 * (coord[1][1] - coord[0][1])) / (coord[1][0] - coord[0][0])
    print m
    return math.degrees(math.atan((0 - m)/(1)))


angle = findAngle(coord)
sinA = math.sin(angle)
cosA = math.cos(angle)
negSin = (-1.0 * sinA)

copy = ndimage.interpolation.rotate(data, angle)
a, b  = np.shape(copy)
print a, b
for row in range(len(data)):
    for col in range(len(data[0])):
        x1 = row * cosA - col*sinA
        y1 = row * sinA + col * cosA
        print x1, y1
        copy[x1][y1] = data[row][col]

#angle = math.radians(90)
#newData = ndimage.interpolation.rotate(data, angle)
#newData = np.rot90(data)
file = open("/Users/daniellenash/Desktop/AlgsPics/majorAxisFlip.txt", "w")

for row in range (0, len(copy)):
        file.write("\n")
        for col in range (0, len(copy[0])):
            file.write("%1i " % copy[row][col])
