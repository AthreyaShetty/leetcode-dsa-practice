"""
Problem: 1137. N-th Tribonacci Number
Link: https://leetcode.com/problems/n-th-tribonacci-number/
Difficulty: Easy
Time Complexity: O(n) 

Space Complexity: O(1) (only 3 variables used)
"""
# Solution 1

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        T0 =  0
        T1 = 1
        T2 = 1

        for i in range(n - 2):
            Tn =  T0 + T1 + T2
            T0 = T1
            T1 = T2
            T2 = Tn
        return T2
    
# Solution 2

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
