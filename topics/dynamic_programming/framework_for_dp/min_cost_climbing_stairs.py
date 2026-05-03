"""
Problem: 746. Min Cost Climbing Stairs
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Difficulty: Easy
Time Complexity: O(n)
    Memoizing the functin improves time complexcity from O(2^n) to O(n) where n is the length of the input array.

Space Complexity: O(n)
"""
# Solution 1

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]

        memo = {}
        return dp(len(cost))
    
# Solution 2

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 0      
            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
        return dp(len(cost))