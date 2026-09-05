class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        ops = "+-/*"

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                op = t
                second = stack.pop()
                first = stack.pop()

                if t == "+":
                    res = first + second 
                elif t == "-":
                    res = first - second 
                elif t == "*":
                    res = first * second
                elif t == "/":
                    res = int(first / second)

                stack.append(res)
        
        return stack[-1]