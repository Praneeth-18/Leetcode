class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            min_idx = i
            for j in range(i, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
        return nums

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Before sorting:", nums)
    solution = Solution()
    sorted_nums = solution.selectionSort(nums)
    print("After sorting:", sorted_nums)

if __name__ == "__main__":
    main()
