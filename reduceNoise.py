import numpy as np
from scipy.ndimage.filters import gaussian_filter

data = np.loadtxt("/Users/daniellenash/Desktop/algorithms-final-project/triangles/tri1.txt")
#blurred = gaussian_filter(data, sigma=7)

#print blurred

minX = []
minY = []
maxX = []
maxY = []
smallestX, smallestY = 0, 0
largeX, largeY = data.shape
avg = 0.0
i =0
j = 0
ones = 0

#print smallestX, smallestY, largeX, largeY

def findBackground(data):
	edges = data[0][0] + data[0][largeY-1] + data[largeX-1][0] + data[largeX-1][largeY-1]
	return (1.0 * edges) / 4

back = findBackground(data)

while i+2 < largeX:
	j = 0
	while j+2 < largeY:
		avg = data[i][j] + data[i+1][j] + data[i+2][j]+ data[i][j+1]+data[i+1][j+1] + data[i+2][j+1] + data[i][j+2] + data[i+1][j+2] + data[i+2][j+2]
		#print avg
		if avg <=2 or (avg >=7 and avg <=8):
			if avg <=2:
				avg = 0
			else:
				avg = 1
			for m in range(2):
				for k in range(2):
					data[i+m][j+k] = avg
		
		else:
			avg = (1.0 * avg)/ 9
			
		if abs(back - avg) > 0.5:
			minX.append(i)
			maxX.append(i+2)
			minY.append(j)
			maxY.append(j +2) 
				
		ones += (avg * 9)
		j+=3
		avg = 0
	i+=3
	
#print data


smallestX, smallestY, largeX, largeY = min(minX), min(minY), max(maxX), max(maxY)
print smallestX, smallestY, largeX, largeY

file = open("/Users/danielleNash/Desktop/AlgsPics/boundBoxT.txt", "w")
			
for a in range(smallestX, largeX-1):
	file.write("\n")
	for b in range(smallestY, largeY-1):
		file.write("%1i " % data[a][b])

file.close()

"""

smallestX, smallestY = 0, 0
largeX, largeY = data.shape
found = [False, False, False, False]
zero = 0
one = 1

for j in range(len(data)):
	for m in range(len(data[0])):
		
		if data[j][m] == 1:
			one += 1
			if j > smallestX:
				smallestX = j
			if j < largeX:
				largeX = j
			if m > smallestY:
				smallestY = m
			if m < largeY:
				largeY = m
		else:
			zero +=1

print smallestX, largeX, smallestY, largeY
file = open("/Users/danielleNash/Desktop/AlgsPics/boundBox.txt", "w")
			
for a in range(smallestX, largeX+1):
	file.write("\n")
	for b in range(smallestY, largeY+1):
		file.write("%1i " % data[a][b])
		

"""
		
		