class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # matching the count number in one string to the other
        # first we store the count for each letter of ransomNote into dictionary
        # then we check magazine has the count of the letters available in ransomNote
        ransomDict = {}
        for l in ransomNote:
            try:
                ransomDict[l] += 1
            except:
                ransomDict[l] = 1
        for key, val in ransomDict.items():
            if magazine.count(key) < ransomDict[key]:
                return False
        return Trues
