class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        # output = 0
        for i in range(len(tokens)):
            token = tokens[i]

            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        stack.append(0)  # Or float('inf') depending on your project rules
                    else:
                        stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]