"""
Problem: 2126. Destroying Asteroids
Link: https://leetcode.com/problems/destroying-asteroids/
Difficulty: Medium
Time Complexity: 

Space Complexity: 
"""

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapq.heapify(asteroids)
        while asteroids:
            asteroid = heapq.heappop(asteroids)
            if mass < asteroid:
                return False
            mass += asteroid
        return True