"""
Problem: 547. Number of Provinces
Link: https://leetcode.com/problems/number-of-provinces/
Difficulty: Meidum
Time Complexity: 

Space Complexity: 
"""

from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)
        return ans