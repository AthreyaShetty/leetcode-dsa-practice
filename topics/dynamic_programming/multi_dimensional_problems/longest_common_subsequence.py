"""
Problem: 1143. Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/
Difficulty: Medium
Time Complexity: O(m.n) work done at each state is O(1)
Space Complexity: O(m.n)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            
            return max(dp(i + 1, j), dp(i, j + 1))
        return dp(0 , 0)