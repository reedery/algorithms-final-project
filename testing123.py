#!/usr/bin/python

# top file test environment

from image import Image
import numpy as np
#import sklearn.neighbors as nei
import sys, os

# 1) denoise
# 2) pixel counts
# 3) bounding box
# 5) find main axis, rotate -> np.roll() ?
# 6) num of corners, determine if polygon or digit
# 7) ???
# 8) profit


# def featuresTest(img):
#     main = Image(np.loadtxt(img))
#     print('W: ' + str(main.width) + '\t' + 'H: ' + str(main.height))
#     main.denoise()
#     print('INVERTED: ' + str(main.inverted))
#     main.setCounts()
#     print('ForegroundPX: ' + str(main.foregroundPixels) + '\t' + ' BackgroundPX: ' + str(main.backgroundPixels))
#     # main.search() // bounding box init
#     return ['empty feature array']


def getFeatures(imgpath):
    # print ('\n' + imgpath)
    main = Image(np.loadtxt(imgpath), imgpath)
    main.denoise()
    main.setCounts()
    main.findMajorAxis()
    main.search()  # bounding box
    main.getSymmetry()
    f = main.makeFeatureVector()
    print('\n' + imgpath)
    print(f)
    return f



# EXAMPLE RUN FORMAT:
# Reede$ python testing123.py /Users/Reede/Desktop/test/database /Users/Reede/Desktop/test/queries /Users/Reede/Desktop/test/output 3
# python /Users/daniellenash/Desktop/algorithms-final-project/testing123/py /Users/daniellenash/Desktop/test/database /Users/daniellenash/Desktop/test/queries /Users/daniellenash/Desktop/test/output 4
# python testing123.py /Users/hoodr/Desktop/algorithms-final-project/database /Users/hoodr/Desktop/algorithms-final-project/query /Users/hoodr/Desktop/algorithms-final-project/output 1
# 
# 
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
        database_map[imgpath] = getFeatures(imgpath)

    query_map = {}
    for img in os.listdir(query):
        imgpath = query + '/' + img
        query_map[imgpath] = getFeatures(imgpath)

    # cluster DB images once, find nearest neighbor foreach in query..