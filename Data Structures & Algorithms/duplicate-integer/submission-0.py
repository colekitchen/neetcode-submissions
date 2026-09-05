class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicates = set(nums)
        if len(noDuplicates) < len(nums):
            return True
        return False