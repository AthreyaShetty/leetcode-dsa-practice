"""
Problem: 876. Middle of the Linked List
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy
Time Complexity: O(N)
    N is the number of nodes in the given list

Space Complexity: O(1) 
    Space used by slow and fast
"""

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow