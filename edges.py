from image import Image
import numpy as np


data = np.loadtxt('triangles/tri7.txt')

i = Image(data)
i.denoise()
path = '/Users/Reede/Desktop/School/Fall \'16/Algos/'
filename = 'tri7_DENOISE.txt'
i.writeOut(path, filename, version='full')
i.search()
fn2 = 'tri7_BOUNDING.txt'
i.writeOut(path, fn2, version='bounded')