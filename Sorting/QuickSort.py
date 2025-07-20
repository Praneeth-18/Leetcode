class Solution:
    def partition(self, nums, low, high):
        i=low
        j=high
        pivot=nums[low]
        while i<j:
            while nums[i]<=pivot and i<=high-1:
                i+=1
            while nums[j]>pivot and j>=low+1:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        nums[low],nums[j]=nums[j],nums[low]
        return j
    
    def quickSortHelper(self, nums, low, high):
        if low < high:
            pidx=self.partition(nums, low, high)
            self.quickSortHelper(nums, low, pidx-1)
            self.quickSortHelper(nums, pidx+1, high)
    
    def quickSort(self, nums):
        n=len(nums)
        self.quickSortHelper(nums,0,n-1)
        return nums
    
def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Before sorting:", nums)
    solution = Solution()
    sorted_nums = solution.quickSort(nums)
    print("After sorting:", sorted_nums)

if __name__ == "__main__":
    main()

