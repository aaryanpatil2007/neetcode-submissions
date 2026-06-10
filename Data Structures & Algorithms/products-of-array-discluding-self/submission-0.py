class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []
        output = []
        for i in range(len(nums)):
            if i == 0:
                prefixes.append(nums[i])
            else:
                prefixes.append(nums[i]*prefixes[i-1])
        
        nums.reverse()

        for i in range(len(nums)):
            if i == 0:
                suffixes.append(nums[i])
            else:
                suffixes.append(nums[i]*suffixes[i-1])

        suffixes.reverse()

        for i in range(len(nums)):
            if i == 0:
                output.append(suffixes[i+1])
            elif i == len(nums) - 1:
                output.append(prefixes[i-1])
            else:
                output.append(prefixes[i-1]*suffixes[i+1])

        return output
            