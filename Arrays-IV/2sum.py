class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        temp=0
        for i,val in enumerate(nums):
            temp = target - val
            if temp in seen:
                return [seen[temp],i]
            seen[val]=i