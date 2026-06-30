class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        list_deque = []
        closing_types = [")", "}", "]"]
        opening_types = ["(", "{", "["]
        full_types = ["()", "{}", "[]"]
        for i in range(len(s)):
            if s[i] in opening_types:
                list_deque.append(s[i])
            elif s[i] in closing_types:
                if not list_deque:
                    return False
                currstring = list_deque.pop()
                if currstring + s[i] not in full_types:
                    return False
        return len(list_deque) == 0