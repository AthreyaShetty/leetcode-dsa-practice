"""
Problem: 199. Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            current_length = len(queue)
            ans.append(queue[-1].val)

            for i in range(current_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans