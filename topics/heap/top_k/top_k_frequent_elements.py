"""
Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
Time Complexity: O(Nlogk) where N is the number of unique elements
Each of the N elements is pushed into and potentially popped from
a heap of size k.

Space Complexity: O(N) to store the frequency map. 
"""

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for  key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val[1] for val in heap ]