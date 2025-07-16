# Find the repeating and missing numbers
# Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        expected_sum, expected_sum_of_squares = (n*(n+1))//2, (n*(n+1)*(2*n+1))//6
        actual_sum, actual_sum_of_squares = 0, 0
        for i in range(n):
            actual_sum += nums[i]
            actual_sum_of_squares += nums[i] * nums[i]
        val1 = actual_sum - expected_sum
        val2 = actual_sum_of_squares - expected_sum_of_squares
        val2 = val2 // val1
        A = (val1 + val2)//2
        B = val2 - A
        return [A,B]