class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            a,b=res[-1]
            c,d=intervals[i]
            if c>=a and c<=b:
                res[-1]=[min(a,b,c,d),max(a,b,c,d)]
            else:
                res.append(intervals[i])
        return res