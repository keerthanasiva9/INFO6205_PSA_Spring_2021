#Set Matrix Zeros

#Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]

#Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def set_matrix_zeros(matrix):
    n = len(matrix[0])
    m = len(matrix)
    arr1 = set()
    arr2 = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i not in arr1:
                    arr1.add(i)
                if j not in arr2:
                    arr2.add(j)

    for k in arr1:
        for j in range(n):
            matrix[k][j] = 0
    for k in arr2:
        for i in range(m):
            matrix[i][k] = 0

    return matrix

if __name__ == '__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print("The input matrix is",matrix)
    print("Output string is:",set_matrix_zeros(matrix))
