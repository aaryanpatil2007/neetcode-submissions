class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        finalarray = [0] * len(temperatures)
        for i in range(len(temperatures)):
            currtemp = temperatures[i]
            if not stack or currtemp <= temperatures[stack[-1]]:
                stack.append(i)
            elif currtemp > temperatures[stack[-1]]:
                while stack and currtemp > temperatures[stack[-1]]:
                    prev = stack.pop()
                    finalarray[prev] = i - prev
                stack.append(i)
        return finalarray


        