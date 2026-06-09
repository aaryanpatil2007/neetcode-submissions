class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in seen.keys():
                seen[char] = seen[char] + 1
            else:
                seen[char] = 1
        for otherchar in t:
            if not otherchar in seen.keys():
                return False
            seen[otherchar] -= 1
        for value in seen.values():
            if value != 0:
                return False    
        return True