"""
Problem: 705. Design HashSet
Link: https://leetcode.com/problems/design-hashset
Difficulty: Easy
"""

# Approach 1: Best for Interview
"""
Complexity:
    Average:
        Add: O(1)
        Remove: O(1)
        Contains: O(1)
    Worst Case: If many keys hash to the same bucket.

"""
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[]for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.table[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.table[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.table[self._hash(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Approach 2 : Best for Leetcode

"""
Complexity:
    Average:
        Add: O(1)
        Remove: O(1)
        Contains: O(1)
        Space: O(10^6)
"""

class MyHashSet:

    def __init__(self):
        self.hashset = [False] * 1000001

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)