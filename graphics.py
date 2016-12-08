__author__ = 'Reede'

# req: Python3 w/ PIL

from PIL import Image, ImageDraw
import random
import pickle
import numpy as np

class ShapeImage(object):
    def __init__(self,  h, w):
        self.h = h
        self.w  = w
        self.color = random.choice([0,1])
        self.im = Image.new('1', (w,h), self.color)
        self.draw = ImageDraw.Draw(self.im)

    def drawShape(self, sides):
        if sides == 4:
            c = self.randomPos(sides)
            self.draw.rectangle(c, fill = random.choice([0,1]), outline = (1-self.color))
            return
        c = self.randomPos(sides)
        self.draw.polygon(c, fill = random.choice([0,1]), outline = (1-self.color))

    def show(self):
        self.im.show()

    def randomPos(self, sides):
        coords = []
        s = sides
        if sides == 4: s = 2
        for i in range(s):
            coords.append((random.randint(0,self.w), random.randint(0,self.h)))
        return coords

shapes = []
for _ in range(1):
    side1 = random.randrange(20,40,2)
    side2 = random.randrange(20,40,2)
    pic = ShapeImage(side1,side2)
    pic.drawShape(3)
    #pic.drawShape(4)
    pic.show()
    dataList = list(pic.im.getdata())
    fullArray = []
    w = pic.w
    h = pic.h
    for i in range(h):
        fullArray.append(dataList[i*w:(w*(i+1))-1])


    print(fullArray)
    data_arr = np.array(fullArray)
    shapes.append(data_arr)

    file = open("/Users/Reede/Desktop/School/Fall '16/Algos/tri9.txt", "w")
    for row in fullArray:
        file.write("\n")
        for item in row:
            file.write(str(item) + " ")
    file.close()

#pickle.dump( shapes, open( "rectangles.algo", "wb" ))