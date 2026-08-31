class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        
        keymap = {}
        keymap["2"] = ["a", "b", "c"]
        keymap["3"] = ["d", "e", "f"]
        keymap["4"] = ["g", "h", "i"]
        keymap["5"] = ["j", "k", "l"]
        keymap["6"] = ["m", "n", "o"]
        keymap["7"] = ["p", "q", "r", "s"]
        keymap["8"] = ["t", "u", "v"]
        keymap["9"] = ["w", "x", "y", "z"]
        newdigits = list(digits)
        returnlist = []
        subset = []
        def dfs(i):
            if i == len(newdigits):
                returnlist.append("".join(subset.copy()))
                return
            currkeys = keymap[newdigits[i]]
            subset.append(currkeys[0])
            dfs(i+1)
            subset.pop()
            subset.append(currkeys[1])
            dfs(i+1)
            subset.pop()
            subset.append(currkeys[2])
            dfs(i+1)
            subset.pop()
            if len(currkeys) > 3:
                subset.append(currkeys[3])
                dfs(i+1)
                subset.pop()

        dfs(0)
        return returnlist
            
            

        

        




