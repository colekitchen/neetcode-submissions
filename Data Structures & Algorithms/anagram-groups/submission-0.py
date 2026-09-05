class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHash = {}

        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in stringHash:
                stringHash[sortedString].append(s)
            else:
                stringHash[sortedString] = [s]

        
        return list(stringHash.values())