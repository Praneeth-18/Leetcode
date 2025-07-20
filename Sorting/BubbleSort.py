class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums)-1, -1, -1):
            swap_done = 0
            for j in range(0, i):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    swap_done = 1
            if swap_done == 0:
                break
        return nums

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Before sorting:", nums)
    solution = Solution()
    sorted_nums = solution.bubbleSort(nums)
    print("After sorting:", sorted_nums)

if __name__ == "__main__":
    main()
