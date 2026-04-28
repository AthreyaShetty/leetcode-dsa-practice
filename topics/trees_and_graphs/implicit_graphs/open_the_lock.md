"""
Problem: 752. Open the Lock
Link: https://leetcode.com/problems/number-of-provinces/
Difficulty: Meidum 
"""


# Overview of the Code

The code defines a class `Solution` with a method `openLock`. The method aims to solve the problem where you need to unlock a "lock" with a 4-digit combination, starting from `"0000"`. The goal is to determine the minimum number of turns required to reach a target combination, considering that some combinations are "deadends" (combinations you cannot visit). The problem is modeled as a graph traversal problem (BFS) to explore all possible valid combinations, and return the number of steps to reach the target.

## Class and Method Setup

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
```

class Solution: This defines a class called Solution.
def openLock(self, deadends: List[str], target: str) -> int: This is the method openLock within the Solution class.
deadends is a list of strings representing combinations that are "deadends" and cannot be used.
target is the target combination we want to reach from the starting combination "0000".
The method returns an integer, which represents the minimum number of turns required to reach the target. If it's impossible, it returns -1.

Helper Function: neighbors

```python
def neighbors(node):
    ans = []
        for i in range(4):
            num = int(node[i])
            for change in [-1, 1]:
                x = (num + change) % 10
                ans.append(node[:i] + str(x) + node[1 + i:])
    return ans    
```

def neighbors(node): This defines an inner function neighbors that returns the "neighbors" of a given combination. In this context, a "neighbor" means a combination that is one step away from the current one (by changing one digit by +1 or -1).
ans = [] Initializes an empty list ans which will store the neighboring combinations.
for i in range(4): This loop iterates through each of the 4 positions of the 4-digit lock.
The index i refers to the current position (0 to 3).
num = int(node[i]) Extracts the digit at position i in the node (the current combination) and converts it to an integer.
for change in [-1, 1]: This nested loop goes through two possible changes for each digit: decrementing (-1) or incrementing (+1).
x = (num + change) % 10 The new value of the digit is computed.
The modulo operation % 10 ensures that the digits "wrap around" (e.g., going from 9 to 0, or from 0 to 9).
ans.append(node[:i] + str(x) + node[1 + i:]) This constructs the new neighbor by:
Taking the portion of the node before the ith digit (node[:i]).
Adding the new digit x (converted to a string).
Appending the portion of the node after the ith digit (node[1 + i:]).
return ans Finally, the function returns the list of all valid neighbors for the current node.


Main Logic

```python
if '0000' in deadends:
            return -1        
```
if '0000' in deadends: This checks if the starting combination "0000" is in the deadends list.

If "0000" is a deadend, it's impossible to start, so the method returns -1 immediately.

```python
queue = deque([('0000', 0)])
seen = set(deadends)
seen.add("0000")        
```

queue = deque([('0000', 0)]) Initializes a queue (using deque for efficient pop from the left) with the starting combination "0000" and a step count of 0. This means we are starting at "0000", with zero steps taken so far.
seen = set(deadends) Initializes a set seen to track visited combinations. It starts with all the deadends because we want to avoid them.
seen.add("0000") Adds the starting combination "0000" to the seen set to mark it as visited.

Breadth-First Search (BFS)

```python
while queue:
    node, steps = queue.popleft()
    if node == target:
        return steps
```

while queue: This is the main loop of the BFS, which continues until all possible nodes are processed or we find the target.
node, steps = queue.popleft() Pops the leftmost element from the queue. Each element is a tuple, where node is the current combination, and steps is the number of steps taken to reach it.
if node == target: If the current combination node matches the target, return the number of steps taken to reach it.

```python
for neighbor in neighbors(node):
    if neighbor not in seen:
        seen.add(neighbor)
        queue.append((neighbor, steps + 1))
```

for neighbor in neighbors(node): For each neighbor of the current node (calculated using the neighbors function).
if neighbor not in seen: If the neighbor has not been visited yet (not in seen).
seen.add(neighbor) Mark the neighbor as visited by adding it to the seen set.
queue.append((neighbor, steps + 1)) Append the neighbor to the queue with an incremented step count (steps + 1).

In the line where we are iterating over neighbors(node), it's important to understand that the neighbors() function returns a list of possible "neighboring" combinations. These combinations are the ones that are one step away from the current combination (node). So, when you iterate over neighbors(node), you're essentially visiting each of these neighboring combinations one by one.

Detailed Explanation:
1. for neighbor in neighbors(node):
This line calls the neighbors() function with the current combination node.
The neighbors() function generates a list of all possible neighboring combinations by changing each of the 4 digits of the current node by +1 or -1.
It then returns this list to the loop, and the for loop iterates over each combination (each neighbor).
2. if neighbor not in seen:
For each neighbor generated, we check if it has already been visited by checking if it exists in the seen set.
If it hasn't been seen before, the code proceeds to mark it as visited and add it to the queue. This ensures that we don't revisit the same combination again.
3. seen.add(neighbor)
This adds the neighbor to the seen set, which helps us keep track of all the combinations we've already processed. This prevents revisiting combinations and ensures that we don't get stuck in cycles.
4. queue.append((neighbor, steps + 1))
Finally, the new neighbor is added to the queue, with the updated steps + 1. This keeps track of how many steps it took to reach the neighbor.
The queue is used for Breadth-First Search (BFS), ensuring we explore all possible combinations level by level, and the first time we reach the target, it will be with the minimum number of steps.


Return -1 if Target is Not Reachable
```python
return -1
```
If the queue is exhausted and the target has not been reached, the function returns -1, indicating that it's impossible to unlock the lock and reach the target combination.
Summary

The function openLock implements a Breadth-First Search (BFS) algorithm to find the shortest path from the starting combination "0000" to the target combination. BFS is ideal here because it explores all combinations level by level (i.e., by number of steps) and guarantees that the first time it finds the target, it will have taken the minimum number of steps.