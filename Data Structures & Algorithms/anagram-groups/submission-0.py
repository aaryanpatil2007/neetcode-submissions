class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # compute some signature for a word so that other words that are
        # anagramic like it can just be added
        keymap = {}
        for i in range(len(strs)):
            if ("").join(sorted(strs[i])) not in keymap.keys():
                keymap[("").join(sorted(strs[i]))] = [strs[i]]
            else:
                keymap[("").join(sorted(strs[i]))].append(strs[i])
        return list(keymap.values())
        
