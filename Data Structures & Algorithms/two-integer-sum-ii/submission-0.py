class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        keymap = {}
        for i in range(len(numbers)):
            keymap[numbers[i]] = i
        for key in keymap.keys():
            otherval = target - key
            if otherval in keymap.keys():
                return [keymap[key] + 1, keymap[otherval] + 1]
        