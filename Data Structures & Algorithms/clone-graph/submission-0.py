"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = collections.deque()
        seen = {}
        queue.append(node)
        seen[node] = Node(node.val)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in seen.keys():
                    seen[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                seen[curr].neighbors.append(seen[neighbor])
        return seen[node]
                

