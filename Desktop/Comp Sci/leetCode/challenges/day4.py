# Rotate Matrix: Given an image represented by an NxN matrix, 
# where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. 
# (Can you do this in place?)

def solve(image):
    result = [ [ 0 for i in range(len(image)) ] for j in range(len(image)) ]
    index = len(result)-1
    index2 = len(result)-1 

    for i in range(len(image)):
        map = image[i]
        for x in range(len(map)):
            result[index2][index] = map[x]
            index2 -= 1
        index -= 1
        index2 = len(result)-1
    
    for i in range(len(result)//2):
        result[i] , result[len(result)-1-i] = result[len(result)-1-i], result[i]
    
    return result

matrix = [[0,1],
          [2,3]]

matrix2 = [[0,1,2],
            [3,4,5],
                [6,7,8]]

matrix3 = [[0,1,2,3],
            [4,5,6,7],
                [8,9,10,11],
                    [12,13,14,15]]

print(solve(matrix3))