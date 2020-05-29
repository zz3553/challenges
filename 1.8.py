def solution(matrix):

    Xindex = 0
    Yindex = 0
    #gets index of first 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                Xindex = x
                Yindex = y

    #puts 0 in other arrays
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y == Yindex:
                matrix[x][y] = 0

    #makes the "all 0" arrays
    for y in range(len(matrix[Xindex])):
        matrix[Xindex][y] = 0


    return matrix
def main():
    matrix = [[0,1,2], [3,4,5], [6,7,8]]
    matrix2 = [[1,2,3], [4,0,5], [6,7,8]]

    print(solution(matrix))
    print(solution(matrix2))

main()