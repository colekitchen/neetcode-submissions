class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.minstack = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.minstack[-1] if self.minstack else val) # Pick the min of the val and the top of the stack, but if the stack is empty just use current val to not error
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        val = self.stack[-1]

        return val

    def getMin(self) -> int:
        return self.minstack[-1]
