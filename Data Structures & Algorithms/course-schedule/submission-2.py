class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist = {}
        for i in range(numCourses):
            adjlist[i] = []
        for crs, pre in prerequisites:
            adjlist[crs].append(pre)

        visited = set()

        def dfs(crs):
            if adjlist[crs] == []:
                return True
            if crs in visited:
                return False
            
            visited.add(crs)

            for course in adjlist[crs]:
                if not dfs(course):
                    return False
                

            visited.remove(crs)
            adjlist[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
            

