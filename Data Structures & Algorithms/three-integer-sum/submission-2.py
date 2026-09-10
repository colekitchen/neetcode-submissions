class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            lp, rp = i + 1, n - 1

            while lp < rp:
                total = nums[i] + nums[lp] + nums[rp]

                if total > 0:
                    rp -= 1
                elif total < 0:
                    lp += 1
                else:
                    triplets.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1

                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp + 1]:
                        rp -= 1
        return triplets