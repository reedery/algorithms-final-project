"""
Converting an Image to Black and White Array

"""
import numpy 

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
	
	#print doubleList

	arg = numpy.array(doubleList)
	print arg
	return arg
	
delim = "\n#\n"
file = open("/Users/danielleNash/Desktop/AlgsPics/output.txt", "w")

file.write(str(makeArray(16, 16, 4, 12, 4, 12)))

file.write(delim)

file.write(str(makeArray(16, 16, 2, 10, 4, 6)))
file.write(delim)
file.write(str(makeArray(16, 16, 3, 10, 1, 9)))
file.write(delim)
file.write(str(makeArray(16, 16, 3, 10, 1, 15)))
file.write(delim)
file.write(str(makeArray(16, 16, 3, 10, 1, 15)))
file.write(delim)
file.write(str(makeArray(16, 16, 2, 14, 8, 12)))
file.write(delim)
file.close()