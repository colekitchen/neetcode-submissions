class Solution:
    def isValid(self, s: str) -> bool:
        bracketHash = {"]":"[", "}":"{", ")":"("}
        openBrackets = "[{("

        stack = collections.deque()

        for b in s:
            if b in openBrackets:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if bracketHash[b] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        
        if len(stack) == 0:
            return True

        return False