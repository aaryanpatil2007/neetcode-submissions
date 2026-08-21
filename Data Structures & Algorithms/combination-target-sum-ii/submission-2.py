class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        finallist = []
        subset = []
        listsort = sorted(candidates)

        def dfs(i, currsum):
            if currsum == target:
                finallist.append(subset.copy())
                return
            if currsum > target or i >= len(listsort):
                return
            save = listsort[i]
            subset.append(save)
            dfs(i+1, currsum + save)
            subset.pop()
            while i + 1 < len(listsort) and listsort[i+1] == listsort[i]:
                i = i + 1
            dfs(i+1, currsum)
        
        dfs(0, 0)
        return finallist

