class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numsHash = {}

        for num in nums:
            if num in numsHash:
                numsHash[num] += 1
            else:
                numsHash[num] = 1
        
        sortedHash = dict(sorted(numsHash.items(), key=lambda item: item[1], reverse=True))

        frequentList = list(sortedHash.keys())

        return frequentList[:k]