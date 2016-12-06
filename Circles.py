import random

def makeCircle():
    width, height = 64, 64
    a, b = random.randint(width/6, 4* width/5), random.randint(height/6, 4* height/5)
    r = min((min(width - a, a -0))/2, (min(height - b, b-0))/2)
    EPSILON = 2.2

    map_ = [[0 for x in range(width)] for y in range(height)]

    # draw the circle
    for y in range(height):
        for x in range(width):
            # see if we're close to (x-a)**2 + (y-b)**2 == r**2
            #if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
            if (x-a)**2 + (y-b)**2 <= r**2:
                map_[y][x] = 1

    return map_

def makeRect():
    width, height = 64, 64
    map_ = [[0 for x in range(width)] for y in range(height)]

    rStart = random.randint(0, (height-2))
    rEnd = random.randint(rStart+2, height-1)
    cStart = random.randint(0, (width-2))
    cEnd = random.randint(cStart+2, width-1)

    
    #Full Rectangle
    for y in range(rStart, rEnd):
        for x in range(cStart, cEnd):
            map_[y][x] = 1
    """
    if rEnd >=height:
        rEnd = height - 1

    if cEnd >=width:
        cEnd = width - 1
    """
    """
    #EmptyRect
    for i in range(rStart, rEnd):
        map_[i][cStart] = 1
        map_[i][cEnd] = 1

    for j in range(cStart, cEnd):
        map_[rStart][j] = 1
        map_[rEnd][j] = 1

    print map_
	"""
    return map_
            

delim = "\n#\n"
fileStart = "/Users/danielleNash/Desktop/AlgsPics/rectangles/fullRect"
#file = open("/Users/danielleNash/Desktop/AlgsPics/emptyRect.txt", "w")

for i in range(50):
    #mymap = makeCircle()
    #print type(mymap)
    fileName = fileStart + str(i) + ".txt"
    file = open(fileName, "w")
    mymap = makeRect()
    #mymap = makeCircle()
    for row in range (0, len(mymap)):
        file.write("\n")
        for col in range (0, len(mymap[0])):
            file.write("%1i " % mymap[row][col])
    file.close()
    
#file.close()
