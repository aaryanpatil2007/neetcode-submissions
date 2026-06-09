class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i in range(len(nums)):
            otherval = target - nums[i]
            if otherval in mapped.keys():
                return [mapped[otherval], i]
            else:
                mapped[nums[i]] = i
                
        

            
