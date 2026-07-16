"""
Problem: 2090. K Radius Subarray Averages
Link: https://leetcode.com/problems/k-radius-subarray-averages/
Difficulty: Easy
Time Complexity: 

Space Complexity:
"""

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        prefix = [nums[0]]
       
        left = 0
        for num in range(1, n):
            prefix.append(nums[num] + prefix[-1])

        for right in range((k * 2) , n):
            ans[right-k] = (prefix[right] - prefix[left] + nums[left]) // ((k * 2) + 1)
            left += 1
        return ans 