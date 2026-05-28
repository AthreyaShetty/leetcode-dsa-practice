"""
Problem: 2208. Minimum Operations to Halve Array Sum
Link: https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
Difficulty: Medium
Time Complexity: O(nlogn + mlogn)
Where n is the number of elements and m is the number of operations required

Space Complexity: O(n) to store the heap
"""

# Solution 1
import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        k = sum(nums) / 2
        heap = [-val for val in nums]
        heapq.heapify(heap)
        s = sum(nums)
        count = 0
        while s > k:
            count += 1
            val = heapq.heappop(heap)
            s -= (-val / 2)
            heapq.heappush(heap, val / 2)
        return count

# Solution 2            
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums)/2
        heap  = [-num for num in nums]
        heapq.heapify(heap)
        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x/2
            heapq.heappush(heap, x/2)
        return ans