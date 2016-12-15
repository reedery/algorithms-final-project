#!/usr/bin/python

# top file test environment
from scipy import spatial
from image import Image
import numpy as np
import sys, os
import kdtree


def getFeatures(imgpath, img):
    # print ('\n' + imgpath)
    main = Image(np.loadtxt(imgpath), set(img))
    main.denoise()
    main.findMajorAxis()
    main.search()  # bounding box
    main.setCounts()
    main.getSymmetry()
    f = main.makeFeatureVector()
    # paths.append(paths)
    # vectors.append(np.ravel(f))
    print('\n' + imgpath)
    print(f)
    return f


# EXAMPLE RUN FORMAT:
# Reede$ python3 testing123.py /Users/Reede/Desktop/test/database /Users/Reede/Desktop/test/queries /Users/Reede/Desktop/test/output 3
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

    imgPaths = []
    vectors = []
    firstVect = []

    database_map = {}
    f = []
    # database calculations...
    for img in os.listdir(db):
        imgpath = db + '/' + img
        f = getFeatures(imgpath, img)
        database_map[imgpath] = f
        firstVect = f
        print
        len(f)

    query_map = {}
    q = []
    counter = 0
    for img in os.listdir(query):
        imgpath = query + '/' + img
        q = getFeatures(imgpath, img)
        database_map[imgpath] = q
        imgPaths.append(imgpath)
        vectors.append(q)
        # for i in range(len(q)):
        # vectors.append(q[i])
        print
        len(q)
        counter += 1

    db_vals = database_map.values()
    tree = kdtree.create(db_vals)
    kdtree.visualize(tree)


