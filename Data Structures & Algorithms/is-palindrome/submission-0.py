class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        for ch in s:
            if ch.isalnum():  # Checks if the character is alphanumeric (letter or number)
                cleanStr += ch
        strLen = len(cleanStr)
        cleanStr = cleanStr.lower()
        for i in range(int(strLen/2)):
            if cleanStr[i] != cleanStr[strLen - 1 - i]:
                return False
        return True