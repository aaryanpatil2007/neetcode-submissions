class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pointer = 0
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    stack.append(b+a)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(b*a)
                elif token == "/":
                    stack.append(int(b/a))
        return stack[0]
            
            