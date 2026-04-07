"""
Problem: 713. Subarray Product Less Than K
Link: https://leetcode.com/problems/subarray-product-less-than-k/
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
"""

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += (right - left) + 1
    return ans