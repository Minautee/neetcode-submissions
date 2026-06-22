class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                # IMPORTANT: The second operand is popped FIRST
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)  # Keeps correct algebraic sign
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # int() on float division correctly truncates toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        return stack[0]
