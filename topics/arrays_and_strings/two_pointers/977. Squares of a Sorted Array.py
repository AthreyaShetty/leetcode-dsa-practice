"""
Problem: 977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy
Time Complexity:
Space Complexity: 
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        for i in range(n - 1, -1, -1):
            if (abs(nums[left])) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square ** 2
        return result