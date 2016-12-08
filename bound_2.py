"""
@Author: Drew Hoo

Bounding box algorithm:
    starting from opposing edges diagonally traverse the image to middle
    search both i,j if one side ends, continue with the other
    return the reshaped image
"""
import numpy as np
import os
import pdb
import traceback

# Initiate the search
def search(image, padding=2, invert=False):
    rows, cols = np.shape(image)
    left_col, top_row = start_top(image, rows, cols, True)
    right_col, bot_row = start_bot(image, rows, cols, True)

    # RESHAPE with the new dims
    r1 = top_row - padding if top_row - padding > 0 else top_row
    r2 = bot_row + padding if bot_row - padding > 0 else bot_row
    c1 = left_col - padding if left_col - padding > 0 else left_col
    c2 = right_col + padding if right_col + padding > 0 else right_col

    row_idx = np.array([x for x in range(r1, r2)])
    col_idx = np.array([x for x in range(c1, c2)])
    
    # MAKE SURE WERE NOT ON THE EDGES OR OVER THE INDEXING
    if col_idx[-1] == cols:
        col_idx = np.delete(col_idx, -1)

    if row_idx[-1] == rows:
        row_idx = np.delete(row_idx, -1)

    # pdb.set_trace()
    # new_image = image[row_idx[:, None], col_idx]
    # print new_image
    # pdb.set_trace()
    # return new_image
    # pdb.set_trace()
    return image[row_idx[:, None], col_idx]

"""
row_idx = np.array([0, 1, 3])
col_idx = np.array([0, 2])
a[row_idx[:, None], col_idx]
"""

# Top always starts at 0,0
def start_top(image, rows, cols, invert=False):
    left_col = []
    top_row = []
    flag = False
    i = 0
    j = 0
    x, y = False, False
    while(not flag):
        while i < rows and j < cols:
            x, y = search_row(image, i, invert), search_col(image, j, invert)
            if x:
                top_row.append(i)
            if y:
                left_col.append(j)
            if x == True and y == True:
                flag = True
            i += 1
            j += 1
        flag = True
    # Assumes we found something
    return left_col[0], top_row[0]

# Bot always starts at shape - 1
def start_bot(image, rows, cols, invert=False):
    right_col = []
    bot_row = []
    i = rows - 1
    j = cols - 1
    flag = False
    x, y = False, False
    while(not flag):
        while i > 0 and j > 0:
            x, y = search_row(image, i, invert), search_col(image, j, invert)
            if x:
                bot_row.append(i)
            if y:
                right_col.append(j)
            if x and y:
                flag = True
            i -= 1
            j -= 1
        flag = True
    # Assumes we found something
    return right_col[0], bot_row[0]

def search_row(image, i, invert):
    fg = 1
    if invert:
        fg = 0
    
    row = image[i,:]
    # SEARCHES SOLELY FOR 1 ans the "other"
    found = np.argwhere(row == fg)
    # print 'found: ', found
    if len(set(found.flatten())) > 1:
        return True
    else:
        return False

    # for x in row:
    #     # TEMP => ADJUST FOR LATER

    #     if x == 1:
    #         return 
    # return

def search_col(image, j, invert):
    fg = 1
    if invert:
        fg = 0
    col = image[:,j]
    # SEARCHES SOLELY FOR 1 ans the "other"
    found = np.argwhere(col == fg)
    # print 'found: ', found
    if len(set(found.flatten())) > 1:
        return True
    else:
        return False

def main(files):
    name = '/Users/hoodr/Desktop/algs_data/out/triangles/output_'
    x = 0
    """
    l = os.listdir(files)
    print type(l)
    print len(l)
    print l
    for file in l:
        if file.endswith('.txt'):
            print file
        else:
            print 'Fail: ', file
    """
    for file in os.listdir(files):
        if file.endswith(".txt"):
            print file
            input_img = np.loadtxt(files + '/' + file)
            refactored = search(input_img)
            np.savetxt(name + str(x) + '.txt', refactored, fmt='%i')
            x += 1
            # pdb.set_trace()
            # print refactored
        else:
            print 'Failed: ', file 

if __name__ == '__main__':
    try:
        # files = "/Users/hoodr/Desktop/algs_data/circles"
        files = "/Users/hoodr/Desktop/algorithms-final-project/triangles"
        main(files)
    except Exception as e:
        # raise e
        traceback.print_exc()