class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        seens1 = {}
        left = 0
        right = len(s1) - 1
        s2map = {}
        for i in range(len(s1)):
            if s1[i] not in seens1.keys():
                seens1[s1[i]] = 1
            else:
                seens1[s1[i]] += 1
        for i in range(0, right + 1):
            if s2[i] not in s2map.keys():
                s2map[s2[i]] = 1
            else:
                s2map[s2[i]] += 1
        while right < len(s2):
            if s2map == seens1:
                return True
            else:
                s2map[s2[left]] -= 1
                if s2map[s2[left]] == 0:
                    del s2map[s2[left]]
                left += 1
                right += 1
                if right < len(s2) and s2[right] not in s2map.keys():
                    s2map[s2[right]] = 1
                elif right < len(s2):
                    s2map[s2[right]] += 1
        return False