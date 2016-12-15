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
    last = []
    count1 = 0 
    going = 1
    
    newCount = 0
    goingCount = 0

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
                cornerList = combineList(cornerList)
                newCount+=1
                """
                if len(cornerList) > 1:
                	last = cornerList.pop()
                	
                	while going > 0:
						if abs(last[0] - y) < 1 or abs(last[1] - x) < 1:
							if r > last[2] and len(cornerList) > 0:
								last = cornerList.pop()
								#cornerList.append([y, x, r])
								going += 1
								goingCount +=1
								count1 +=1
								count-=1
							else:
								cornerList.append(last)
								going = 0
						
						else:
							
							if going ==1:
								cornerList.append(last)
								
							cornerList.append([y, x, r])
							count +=1
							
							going = 0
							#count +=1
                else:
               		cornerList.append([y, x, r])
               		newCount +=1
                """
                
            

    #print "New Count:", newCount, "Going Count:", goingCount
    return cornerList

def combineList(list):
	if len(list) < 2:
		return list
	
	comp = list.pop()
	last = list.pop()
	
	going = 1
	
	while going >= 1:
		
		if abs(comp[0] - last[0]) < 4 or abs(comp[1] - last[1]) < 4:
			
			if comp[2] > last[2]:
				if len(list) > 1:
					last = list.pop()
				else:
					list.append(comp)
					going = 0
			else:
				if len(list) > 1:
					comp = last
					last = list.pop()
				else:
					list.append(last)
					going = 0
		else:
			list.append(last)
			list.append(comp)
			going = 0
	
	#print len(list)
	return list


data1 = np.loadtxt("/Users/daniellenash/Documents/smallA.txt")
data2 = np.loadtxt("/Users/daniellenash/Desktop/algorithms-final-project/rectangles/fullRect10.txt")
data3 = np.loadtxt("/Users/daniellenash/Desktop/algorithms-final-project/circles/fullCircle10.txt")
data4 = np.loadtxt("/Users/daniellenash/Desktop/algorithms-final-project/triangles/tri4.txt")

print "A"
print findCorners(data1, 4, 0.05, 1)
print "Rectangle"
print findCorners(data2, 4, 0.05, 1)
print "Circle"
print findCorners(data3, 4, 0.05, 1)
print "Triangle"
print findCorners(data4, 4, 0.05, 1)




