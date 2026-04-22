class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+', '-', '*', '/'}
        stack = []
        for s in tokens:
            if s in op:
                b = stack.pop()
                a = stack.pop()
                if s == '*':
                    rslt = a * b
                elif s == '+':
                    rslt = a + b
                elif s == '-':
                    rslt = a - b
                else:
                    rslt = int(a/b)
                
                stack.append(rslt)
            else: 
                stack.append(int(s))

        return stack[-1]