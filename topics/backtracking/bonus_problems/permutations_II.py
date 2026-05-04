"""
Problem: 47. Permutations II
Link: https://leetcode.com/problems/permutations-ii/
Difficulty: Medium
Time Complexity: O(summation k=1 to N , P(N, k))
                P(N, k) = (N! / (N - k)!)
Space Complexity: O(N)
                Hash Table: worst case where each number is unique O(N)
                Callstack for recursion, O(N) for recursion
                Permutation takes another O(N)
                O(N) + O(N) + O(N) =  O(N)
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)

                    comb.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return results