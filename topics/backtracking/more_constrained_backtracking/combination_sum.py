"""
Problem: 39. Combination Sum
Link: https://leetcode.com/problems/combination-sum/
Difficulty: Medium
Time Complexity: O(n ^ T/M) 
                n = length of the candidates
                T = Target
                M = min(candidates)
                The maximum depth of a tree in this problem is T/M - using the smallest number repeatedly until we exceed
                target. Each node in the tree can have up to n children, which gives us O(n ^ T/M) 

Space Complexity: O(T/M) 
                If not counting the output as extra space, the space used in this problem is for path, and
                recursion call stack, both of which are O(T/M)  
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, start, curr):
            if curr == target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if curr + candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(path, i, curr + candidates[i])
                    path.pop()
        ans = []
        backtrack([], 0, 0)
        return ans