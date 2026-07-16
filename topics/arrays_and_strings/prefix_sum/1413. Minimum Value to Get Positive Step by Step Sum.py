"""
Problem: 1413. Minimum Value to Get Positive Step by Step Sum
Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Difficulty: Easy
Time Complexity: 

Space Complexity:
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minval = total = 0
        for i in nums:
            total += i
            minval = min(minval, total)
        return -minval + 1