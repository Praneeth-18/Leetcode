# You are given an n x n 2D matrix representing an image,
# Rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place,
# which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row in place
        for i in range(n):
            matrix[i].reverse()

def print_matrix(m: List[List[int]]) -> None:
    for row in m:
        print(row)
    print()

if __name__ == "__main__":
    # example usage
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("Before:")
    print_matrix(matrix)

    Solution().rotate(matrix)

    print("After 90° clockwise:")
    print_matrix(matrix)
