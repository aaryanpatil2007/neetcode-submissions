class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        newlist = []
        stack = []
        checker = []
        for i, j in zip(position, speed) :
            newlist.append([i, j])
        newlist.sort(key=lambda x: x[0])
        for thing in newlist:
            time = (target - thing[0]) / thing[1]
            stack.append(time)
        while stack:
            curr = stack.pop()
            if not checker:
                checker.append(curr)
            else:
                check = checker[-1]
                if curr > check:
                    checker.append(curr)   
        return len(checker)
        