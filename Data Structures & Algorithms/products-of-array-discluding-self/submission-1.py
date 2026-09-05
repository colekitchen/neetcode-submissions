class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totProduct = 1
        zeroCount = 0
        prodArray = []
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                totProduct *= num
        
        if zeroCount > 1:
            prodArray = [0] * len(nums)
        elif zeroCount == 1:
            for num in nums:
                if num == 0:
                    prodArray.append(totProduct)
                else:
                    prodArray.append(0)
        else:
            for num in nums:
                prodArray.append(totProduct // num)
            
        
        return prodArray