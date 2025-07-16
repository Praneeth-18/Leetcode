# Given an integer numRows, return the first numRows of Pascal's triangle.
class Solution:
    def nCr(self,n,r):
        res=1
        for i in range(r):
            res = res*(n-i)
            res = res//(i+1)
        return res
    
    def row(self,m):
        ans=[]
        for i in range(m+1):
            ans.append(self.nCr(m,i))
        return ans
    
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(1,numRows):
            l.append(self.row(i))
        return l