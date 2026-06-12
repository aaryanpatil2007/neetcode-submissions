class Solution:
    def isPalindrome(self, s: str) -> bool:
        builder = []
        for i in range(len(s)):
            if s[i].isalnum():
                builder.append(s[i].lower())
        builder = "".join(builder)
        left = 0
        right = len(builder) - 1
        while left < right:
            if builder[left] != builder[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
            
