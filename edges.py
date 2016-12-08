from image import Image
import numpy as np


data = np.loadtxt('triangles/tri9.txt')

i = Image(data)

print(i.data)