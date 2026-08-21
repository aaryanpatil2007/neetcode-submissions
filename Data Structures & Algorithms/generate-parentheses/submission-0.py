class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        finallist = []
        subset = []
        open_count = 0
        close_count = 0

        def dfs(open_count, close_count):
            if open_count > n:
                return
            if close_count > open_count:
                return
            if open_count == n and close_count == n:
                finallist.append("".join(subset.copy()))
                return
        
            subset.append("(")
            open_count += 1
            dfs(open_count, close_count)
            subset.pop()
            open_count -= 1
            subset.append(")")
            close_count += 1
            dfs(open_count, close_count)
            subset.pop()
            close_count -= 1
        
        dfs(open_count, close_count)

        return finallist
