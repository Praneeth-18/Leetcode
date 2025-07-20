class Solution:
    def insertionSort(self, nums):
        for i in range(len(nums)):
            j=i
            while j>0 and nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        return nums

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Before sorting:", nums)
    solution = Solution()
    sorted_nums = solution.insertionSort(nums)
    print("After  sorting:", sorted_nums)
