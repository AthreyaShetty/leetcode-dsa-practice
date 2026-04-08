"""
Problem: 24. Swap Nodes in Pairs
Link: https://leetcode.com/problems/swap-nodes-in-pairs/
Difficulty: Medium
Time Complexity: O(n)
    n is the number of nodes in the linked list
    while loop runs n times
    work done at each iteration is O(1)

Space Complexity: O(1) 
    we are only using few pointers
    
"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        dummy = head.next
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head

            next_node = head.next.next
            head.next.next = head
            head = next_node
            prev.next = head
        return dummy