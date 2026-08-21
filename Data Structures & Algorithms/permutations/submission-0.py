class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finallist = []
        subset = []
        globset = set()
        def dfs(i):
            if len(subset) == len(nums):
                finallist.append(subset.copy())
                return
            for j in range(len(nums)):
                if not nums[j] in globset:
                    subset.append(nums[j])
                    globset.add(nums[j])
                    dfs(j + 1)
                    subset.pop()
                    globset.remove(nums[j])
        
        dfs(0)

        return finallist
            
            




        

            