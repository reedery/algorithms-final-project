"""
Super Basic way to make squares and save them in a text file
Makes random squares, which we can later shift and rotate

By: Danielle

"""
import numpy as np
import random

## Size is 128 x 128

def returnRow(totalSize, onesStart, onesEnd):
	row = []
	for i in range(totalSize):
		if(i >= onesStart and i < onesEnd):
			row.append(1)
		else:
			row.append(0)
		
	return row

def makeArray(rowSize, colSize, rStart, rEnd, cStart, cEnd):	
	
	doubleList = []
	for i in range(rStart):
		doubleList.append(returnRow(rowSize, -1, -1))
	for i in range(rEnd - rStart): 
		doubleList.append(returnRow(rowSize, cStart, cEnd))
	for i in range(colSize - rEnd):
		doubleList.append(returnRow(rowSize, -1, -1))
	
	arg = np.array(doubleList)
	#print arg
	return arg
	
delim = "\n#\n"
file = open("/Users/danielleNash/Desktop/AlgsPics/output.txt", "w")

height = 16
width = 38

for i in range(35):
	rStart = random.randint(0, (height-2))
	rEnd = random.randint(rStart+2, height)
	cStart = random.randint(0, (width-2))
	cEnd = random.randint(cStart+2, width)
	
	#array1 = makeArray(height, width, rStart, rEnd, cStart, cEnd)
	#outputFile = 'output_main' + str(i) + ".txt"
	#file.write(str(makeArray(height, width, rStart, rEnd, cStart, cEnd)))
	#file.write(delim)
	array = makeArray(width, height, rStart, rEnd, cStart, cEnd)
	for row in range (0, height):
		 file.write("\n")
		 for col in range (0, width):
			  file.write("%1i" %array [row][col])
	file.write(delim)
			
	

file.close()