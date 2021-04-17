#Rotate Image

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#DO NOT allocate another 2D matrix and do the rotation.

#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

#Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

def rotate_image(matrix):
    if matrix is None:
        return None

    n = len(matrix)
    if n == 1:
        return matrix

    for i in range(n):
        if len(matrix[i]) != n:
            raise Exception("Matrix must be square")

    # Transpose the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Swap columns
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    return matrix
if __name__ == '__main__':
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print("The input matrix is",matrix)
    print("Output string is:",rotate_image(matrix))
