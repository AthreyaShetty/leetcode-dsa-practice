"""
Problem: 1004. Max Consecutive Ones III
Link: https://leetcode.com/problems/max-consecutive-ones-iii/
Difficulty: Medium
Time Complexity: 
Space Complexity: 

Pattern:
Sliding Window
------------------------
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans