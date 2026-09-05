class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = collections.deque()
        maxA = 0

        for i, h in enumerate(heights):
            newI = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxA = max(maxA, (i - index)*height)
                newI = index
            stack.append((newI, h))
        
        for i, h in stack:
            maxA = max(maxA, h * (len(heights) - i))
            
        return maxA