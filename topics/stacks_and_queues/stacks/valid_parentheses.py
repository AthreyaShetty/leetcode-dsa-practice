"""
Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Time Complexity: 

Space Complexity: 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'{': '}','(':')', '[':']'}
        stack = []
        for bracket in s:
            if bracket in matching:
                stack.append(bracket)
            elif stack:
                prev_bracket = stack.pop()
                if matching[prev_bracket] != bracket:
                    return False
            else:
                return False
        return not stack