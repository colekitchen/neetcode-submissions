class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totProduct = 1
        zeroCount = 0
        prodArray = []

        for n in nums:
            if n == 0:
                zeroCount+=1
            else:
                totProduct *= n
        
        if zeroCount > 1:
            return [0] * len(nums)
        elif zeroCount == 1:
            for n in nums:
                if n == 0:
                    prodArray.append(totProduct)
                else:
                    prodArray.append(0)
        else:
            for n in nums:
                prodArray.append(totProduct // n)
        
        return prodArray