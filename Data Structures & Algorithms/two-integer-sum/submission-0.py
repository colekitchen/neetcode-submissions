class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}

        for i, num in enumerate(nums):
            goal = target - num
            if goal in numHash:
                return [numHash[goal], i]
            numHash[num] = i