"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Time Complexity: O(n.m.logm)
    n - length of strs
    m - average length of strings
    We iterate over each string and sort it
    Worst case scenario: NO matching anagrams, then there will be n groups. O(n)


Space Complexity: O(n.m)
    Each string will be placed in an array within the hash map
"""

# Solution 1:
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            skey = "".join(sorted(s))
            groups[skey].append(s)
        
        return list(groups.values())


# Solution 2:
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            skey = "".join(sorted(s))
            groups[skey].append(s)
        
        ans = []
        for key, val in groups.items():
            ans.append(val)
        return ans
    
