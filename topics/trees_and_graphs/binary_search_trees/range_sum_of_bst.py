"""
Problem: 938. Range Sum of BST
Link: https://leetcode.com/problems/range-sum-of-bst/
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        ans = 0
        if low <= root.val <= high:
            ans += root.val
        
        if low < root.val:
            ans += self.rangeSumBST(root.left, low, high)
        if high > root.val:
            ans += self.rangeSumBST(root.right, low, high)
        
        return ans
    
# Solution 2
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        asn = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            
            if node.left and node.left > low:
                stack.append(node.left)
            if node.right and node.right < high:
                stack.append(node.right)
        return ans