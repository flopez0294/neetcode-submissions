class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        if len(s) == 0: return True
        mp = []
        lis = {'(': ')', '[':']', '{':'}'}
        mp.append(s[0])
        for i in s[1:]:
            if i in "([{" or len(mp) == 0:
                mp.append(i)
            elif lis.get(mp.pop()) != i:
                return False
            

        return len(mp) == 0

