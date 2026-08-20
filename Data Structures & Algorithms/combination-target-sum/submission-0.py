class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        finallist = []
        subset = []

        def dfs(i):
            if sum(subset) == target:
                finallist.append(subset.copy())
                return
            if sum(subset) > target or i >= len(nums):
                return
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return finallist
