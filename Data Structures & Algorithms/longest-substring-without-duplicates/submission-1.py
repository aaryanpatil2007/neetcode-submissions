class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            currlen = 0
            seen = set()
            while i < len(s) and s[i] not in seen:
                seen.add(s[i])
                currlen += 1
                i += 1
            maxlen = max(currlen, maxlen)
        return maxlen