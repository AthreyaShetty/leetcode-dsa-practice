"""
Problem: 203. Remove Linked List Elements
Link: https://leetcode.com/problems/remove-linked-list-elements/
Difficulty: Easy
Time Complexity: 

Space Complexity: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:        
        if head:
            while head.val == val:
                head = head.next
                if not head:
                    return head 
        prev = node = head
        while node:
            while node.val == val:
                prev.next = node.next
                if node.next:
                    node = node.next
                else: break
        
            prev = node
            node = node.next
        return head