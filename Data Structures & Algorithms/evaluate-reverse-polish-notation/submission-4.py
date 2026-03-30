import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                if token == "-":
                    stack.append(num1 - num2)
                if token == "*":
                    stack.append(num1 * num2)
                if token == "/":
                    stack.append(int(num1 / num2))
            
        return stack[0]