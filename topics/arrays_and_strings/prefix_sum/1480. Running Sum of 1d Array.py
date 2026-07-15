"""
Problem: 1480. Running Sum of 1d Array
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Difficulty: Easy
Time Complexity: 

Space Complexity:
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+ prefix[-1])
        return prefix