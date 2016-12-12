#!/usr/bin/python

# top file test environment

from image import Image
import numpy as np
import sys, os

# 1) denoise
# 2) pixel counts
# 3) bounding box
# 5) find main axis, rotate -> np.roll() ?
# 6) num of corners, determine if polygon or digit
# 7) ???
# 8) profit


def features(img):
    main = Image(np.loadtxt(img))
    print('W: ' + str(main.width) + '\t' + 'H: ' + str(main.height))
    main.denoise()
    print('INVERTED: ' + str(main.inverted))
    main.setCounts()
    print('ForegroundPX: ' + str(main.foregroundPixels) + '\t' + ' BackgroundPX: ' + str(main.backgroundPixels))
    # main.search() // bounding box init
    return ['empty feature array']

def getNeighbors(img, k, dataset):
    targetVector = features(img)
    # cluster()
    # get neighbors...
    # ...
    return ['the knn...']


# EXAMPLE RUN FORMAT:
# Reede$ python testing123.py /Users/Reede/Desktop/test/database /Users/Reede/Desktop/test/queries /Users/Reede/Desktop/test/output 3

if __name__ == '__main__':
    """"
    cmd line args:
        0: unused (name of .py file)
        1: path to database of images
        2: path to query images
        3: path to output file
        4: k
    """
    cmdline_args = sys.argv
    db = cmdline_args[1]
    query = cmdline_args[2]
    output_path = cmdline_args[3]
    k = cmdline_args[4]

    database_map = {}
    # database calculations...
    for img in os.listdir(db):
        imgpath = db + '/' + img
        print(imgpath)
        database_map[imgpath] = getNeighbors(imgpath, k, db)
        print('\n')
