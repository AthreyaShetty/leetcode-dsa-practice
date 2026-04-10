"""
Problem: 2270. Number of Ways to Split Array
Link: https://leetcode.com/problems/number-of-ways-to-split-array/
Difficulty: Medium
Time Complexity: O(n.m.logm)
    n - length of strs
    m - average length of strings
    We iterate over each string and sort it
    Worst case scenario: NO matching anagrams, then there will be n groups. O(n)


Space Complexity: O(n.m)
    Each string will be placed in an array within the hash map
"""

# Solution 1:
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSumArray = [nums[0]]
        for i in range(1,len(nums)):
            prefixSumArray.append(nums[i] + prefixSumArray[-1])

        ans = 0
        for i in range(len(nums) - 1):
            if prefixSumArray[i] >= prefixSumArray[-1] -prefixSumArray[i]:
                ans += 1
        return ans

# Solution 2:
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        curr = 0
        ans = 0
        for i in range(len(nums) - 1):
            curr += nums[i]
            if curr >= totalSum - curr:
                ans += 1
        return ans

