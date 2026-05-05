"""
Problem: 875. Koko Eating Bananas
Link: https://leetcode.com/problems/koko-eating-bananas/
Difficulty: Medium
Time Complexity: 

Space Complexity: 
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)
            return hours <= h

        left =  1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else: left = mid + 1
        return left