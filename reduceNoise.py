import numpy as np
from scipy.ndimage.filters import gaussian_filter

data = np.loadtxt("/Users/daniellenash/Desktop/AlgsPics/fullRect.txt")


smallestX = float('inf')
smallestY = float('inf')
largeX, largeY = 0, 0
found = [False, False, False, False]
zero = 0
one = 1

for j in range(len(data)):
	for m in range(len(data[0])):
		if data[j][m] == 1:
			one += 1
			if j < smallestX:
				smallestX = j
			if j > largeX:
				largeX = j
			if m < smallestY:
				smallestY = m
			if m > largeY:
				largeY = m
		else:
			zero +=1

print smallestX, largeX, smallestY, largeY
file = open("/Users/danielleNash/Desktop/AlgsPics/boundBox.txt", "w")
			
for a in range(smallestX, largeX+1):
	file.write("\n")
	for b in range(smallestY, largeY+1):
		file.write("%1i " % data[a][b])
		

		
		
		