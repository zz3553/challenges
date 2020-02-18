def solution(matrix):

    for x in range(len(matrix)):
        matrix[0][x], matrix[len(matrix)-1][x] = matrix[len(matrix)-1][x], matrix[0][x]

    for x in range(len(matrix)):
        for q in range(1, len(matrix[x])):
            num1 = matrix[x][q]
            num2 = matrix[q][x]
            matrix[x][q], matrix[q][x] = matrix[q][x], matrix[x][q]

    return matrix

def main():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(matrix)
    print(solution(matrix))

main()