# Given an m x n matrix, return all elements of the matrix in spiral order.
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        bottom = len(matrix)-1
        top=0
        left = 0
        right = len(matrix[0])-1
        final_list=[]
        while top<=bottom and left<=right:
            for col in range(left, right+1):
                final_list.append(matrix[top][col])
            top+=1
            for row in range(top, bottom+1):
                final_list.append(matrix[row][right])
            right-=1
            if top<=bottom:
                for col in range(right,left-1,-1):
                    final_list.append(matrix[bottom][col])
                bottom-=1
            if left<=right:
                for row in range(bottom,top-1,-1):
                    final_list.append(matrix[row][left])
                left+=1
        return final_list
            
if __name__ == "__main__":
    # quick demos
    tests = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [[1]],
        [[1],[2],[3]],
    ]

    sol = Solution()
    for i, mat in enumerate(tests, 1):
        print(f"Test {i}: {mat} -> {sol.spiralOrder(mat)}")
