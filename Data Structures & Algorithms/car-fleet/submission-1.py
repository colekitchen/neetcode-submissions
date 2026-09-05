class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        stack = collections.deque()

        for i in range(len(speed)):
            cars.append([position[i], speed[i]]) # Cars that contain their position and speed

        cars = sorted(cars, reverse=True)
        
        for c in cars:
            stack.append(c)
            if len(stack) > 1:  
                if ((target - c[0])/c[1]) <= ((target - stack[-2][0])/stack[-2][1]):
                    stack.pop()
        
        return len(stack)
    

