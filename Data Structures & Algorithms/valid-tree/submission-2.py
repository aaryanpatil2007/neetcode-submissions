class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #if there's a cycle its wrong
        if n == 1:
            return True
        adjlist = {}
        for i in range(n):
            adjlist[i] = []
        
        for ins, out in edges:
            adjlist[ins].append(out)
            adjlist[out].append(ins)
        
        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False
            if adjlist[node] == []:
                return True
            
            visited.add(node)

            for out in adjlist[node]:
                if out == parent:
                    continue
                elif not dfs(out, node):
                    return False
            return True

        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n

        
        