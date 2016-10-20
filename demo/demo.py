def makeArrays():
    n = random.choice([12,13,14])
    m = random.choice([12,13,14])
    images = []
    for i in range(4):
        images.append(np.random.randint(2, size=(n, m)))
    return images   

def getScore(testImage, mainImage):
    similar = 0
    for i in range(len(testImage)):
        for j in range(len(testImage[0])):
            if(testImage[i][j] == mainImage[i][j]):
                similar += 1
    return similar
    
    
if __name__ == "__main__":
    import numpy as np
    import random
    import scipy.ndimage as sc

    try:
        images = makeArrays()
        """print("inputs:")
        for image in images:
            print(image)
        """
    except Exception as e:
        print (e)
        
    mainImage = images.pop(0)

    totalScores = []
    for image in images:
        scores = []
        for i in range(2):
            scores.append((getScore(image, mainImage), image ))
            scores.append((getScore(np.fliplr(image), mainImage), np.fliplr(image)))
            scores.append((getScore(np.flipud(image), mainImage), np.flipud(image)))
            image = sc.rotate(image, 180)
        max_tuple = max(scores, key = lambda x:int(x[0]))

        print ("max score, transform \n", max_tuple)
        totalScores.append(max_tuple)
    
    
    print ("\nTotal Scores: \n", totalScores)
    print ("\nMain Image\n", mainImage)
    #print ("\nClosest Image\n", images[totalScores.index(max(totalScores))])
    print ("\nClosest Image\n", max(totalScores)[1])
        