"""
Problem: 1046. Last Stone Weight
Link: https://leetcode.com/problems/last-stone-weight/
Difficulty: Easy
Time Complexity: 

Space Complexity: 
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -abs(y - x))
        return -heap[0] if heap else 0