import numpy as np
from image import Image
import os

""""
@Author: Ryan Reede
12/8/16
test/development file for Denoising functions
in the Image class

"""

def encodeValues(vals):
    """"
    Determine if the values given as input are all ONE,
    ZERO or MIX. Encoded as follows:
        00 = all ZERO, 01 = MIX and 11 = all ONE
    """
    if vals.count(vals[0]) == len(vals):
        if vals[0] == 0:
            return '00'
        return '11'
    return '01'


def checkWindow(posY, posX, image):
    """"
    #TODO: parameterize this function for larger window sizes
    Checks 4x4 matrix from around specified X and Y coords
        that wraps around any edge of the given image's
        data matrix for noise removal. Will check
    Returns:
        - 4x4 matrix from around specified X and Y coords
            that wraps around any edge of the given image's
            data matrix for noise removal.
        - list of x/y indices that are in the middle of the
            4x4 matrix
        - 2-bit encoding where 00 = all ZERO, 01 = MIX and
            11 = all ONE. These values refer to what is on
            the outside edges of the 4x4 matrix
    """
    data = image.data
    height = image.height
    width = image.width
    outsideValues, insideIndices, final = [], [], []
    for c in range(4):
        posX_new = (posX + c) % height
        c_list = []
        for r in range(4):
            posY_new = (posY + r) % width
            c_list.append(data[posX_new][posY_new])
            if r == 1 or r == 2: # check to make sure we're in the middle
                if c == 1 or c == 2:
                    insideIndices.append([posY_new, posX_new])
        final.append(c_list)
        if c == 0 or c == 3:
            outsideValues.extend(c_list)
        else:
            outsideValues.extend([c_list[0], c_list[3]])
    return final, insideIndices, encodeValues(outsideValues)


def changeValues(image, indicies, number):
    for xyPair in indicies:
        image.data[xyPair[1]][xyPair[0]] = number


def denoise(im):
    # make 4x4 chunks, if center is dif from surrounding, make it the same as surrounding.
    for w in range(0, im.width):
        for h in range(0, im.height):
            final, insides, code = checkWindow(w, h, im)
            if code != '01':
                if code == '00':
                    changeValues(im, insides, 0)
                else:
                    changeValues(im, insides, 1)




i = np.asarray([
         [1,1,0,0,0,0,0,0],
         [1,1,0,0,0,0,0,0],
         [0,0,1,1,1,1,0,0],
         [0,0,1,1,1,1,0,0],
         [0,0,1,1,0,1,0,0],
         [0,0,1,1,1,1,0,0],
         [0,0,1,1,1,1,0,0],
         [0,0,1,0,1,1,0,0],
         [0,0,1,0,0,1,0,0],
         [0,0,1,1,1,1,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,1,1],
         [0,0,0,1,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,0,0],
         [0,0,1,0,0,1,0,0],
         [0,0,1,0,0,1,0,0],
         [1,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,0]])


p = np.asarray([
    [0,1,2,3,4,5,6,7,8],
    [1,2,0,4,5,6,7,8,9],
    [2,9,4,5,4,7,8,9,0],
    [3,4,3,6,7,8,9,0,1],
    [4,5,6,7,8,9,0,1,2],
    [5,6,7,8,9,0,1,2,3],
    [6,7,8,9,0,1,2,3,4],
    [7,8,9,0,1,2,3,4,5],
    [8,9,0,1,2,3,4,5,6],
    [9,0,1,2,3,4,5,6,7],
    [0,1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8,9]])



myImage = Image(i)
denoise(myImage)
print(myImage.data)















