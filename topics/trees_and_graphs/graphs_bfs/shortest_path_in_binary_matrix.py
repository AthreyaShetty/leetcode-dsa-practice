"""
Problem: 1091. Shortest Path in Binary Matrix
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Difficulty: Medium
Time Complexity: 

Space Complexity: 
"""

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        n = len(grid)
        seen =  {(0, 0)}
        queue = deque([(0, 0, 1)])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                    queue.append((next_row, next_col, steps + 1))
                    seen.add((next_row, next_col))
        return -1