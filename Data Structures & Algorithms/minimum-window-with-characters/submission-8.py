class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        th = {}
        for c in t:
            th[c] = th.get(c, 0) + 1

        sh = {}

        left = 0
        best = ""

        def valid():
            for c in th:
                if sh.get(c, 0) < th[c]:
                    return False
            return True

        for right in range(len(s)):
            c = s[right]
            sh[c] = sh.get(c, 0) + 1

            while valid():
                window = s[left:right+1]

                if best == "" or len(window) < len(best):
                    best = window

                sh[s[left]] -= 1
                left += 1

        return best