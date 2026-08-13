class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        
        for ins, out in edges:
            adjlist[ins].append(out)
            adjlist[out].append(ins)
        
        counter = 0

        visited = set()
        
        def dfs(node):
            visited.add(node)
            
            for other in adjlist[node]:
                if other not in visited:
                    dfs(other)
        
        for i in range(n):
            if i not in visited:
                counter += 1
                dfs(i)
        
        return counter

