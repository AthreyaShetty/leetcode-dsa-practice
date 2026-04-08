"""
Problem: 2248. Intersection of Multiple Arrays
Link: https://leetcode.com/problems/intersection-of-multiple-arrays/
Difficulty: Easy
Time Complexity: O(m.(n + log(m))
    n - number of sub lists in the main list
    m - average number of elements in the sublists
    To populate the hash map it costs:         O(n.m)
    Sorting of atmost m elements will cost:    O(m.log(m))
    Hence, Time Complexity:                    O(n.m) + O(m.log(m)) = O(m.(n + log(m))

Space Complexity: O(n.m)
    If every element in the input is unique, then hashmap will grow to the size of n.m 
"""

def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        ans = []
        n = len(nums)
        for arr in nums:
            for x in arr:
                counts[x] += 1
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        return sorted(ans)