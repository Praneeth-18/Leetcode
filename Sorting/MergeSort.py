class Solution:
    def mergeSort(self, nums):
        low=0
        high=len(nums)-1
        self.mergeSortHelper(nums, low, high)
        return nums
        
    def mergeSortHelper(self, nums, low, high):
        if low==high:
            return
        mid=(low+high)//2
        self.mergeSortHelper(nums,low, mid)
        self.mergeSortHelper(nums,mid+1,high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        temp=[]
        left=low
        right=mid+1
        while left<=mid and right<=high:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i]=temp[i-low]
        
def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Before sorting:", nums)
    solution = Solution()
    sorted_nums = solution.mergeSort(nums)
    print("After sorting:", sorted_nums)

if __name__ == "__main__":
    main()
