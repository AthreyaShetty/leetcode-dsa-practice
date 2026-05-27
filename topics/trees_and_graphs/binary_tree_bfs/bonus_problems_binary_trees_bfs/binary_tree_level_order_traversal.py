"""
Problem: 102. Binary Tree Level Order Traversal
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Time Complexity: 

Space Complexity: 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque([root])
        ans = [[root.val]]
        while queue:
            curr_len = len(queue)
            arr = []
            for x in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    arr.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    arr.append(node.right.val)
            if arr: ans.append(arr)
        return ans