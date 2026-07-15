"""
Problem: 643. Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Sliding Window
------------------------
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = ans = 0
        for i in range(k):
            curr += nums[i]
        ans = curr / k
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr/k)
        return ans