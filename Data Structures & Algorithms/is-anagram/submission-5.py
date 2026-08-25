class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        firstWord = defaultdict(int)
        secondWord = defaultdict(int)

        for i in s:
            firstWord[i] = firstWord.get(i, 0) + 1
        
        for i in t:
            secondWord[i] = secondWord.get(i, 0) + 1
        
        for i in firstWord.keys():
            if firstWord[i] != secondWord.get(i, 0):
                return False
        return True

        