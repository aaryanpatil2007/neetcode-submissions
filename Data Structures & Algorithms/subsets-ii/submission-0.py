class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        finallist = []
        subset = []
        newlist = sorted(nums)
        def dfs(i):
            if i >= len(newlist):
                finallist.append(subset.copy())
                return
    
            subset.append(newlist[i])
            dfs(i + 1)
            while i < len(newlist) - 1 and newlist[i+1] == newlist[i]:
                i = i + 1
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return finallist

