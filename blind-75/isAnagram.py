# 242. Valid Anagram
def isAnagram(self, s: str, t: str) -> bool:
        
        # Create an empyt dictionary to keep track of the occurance of each letter
        # { a: 1, b: 2}
        
        countS, countT = {}, {}
        # if s and t are anagram -> they must have same length
        if len(s) != len(t):
            return False

        for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True