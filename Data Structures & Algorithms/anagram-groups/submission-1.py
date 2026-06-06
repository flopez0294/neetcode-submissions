class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        
        dic = {}
        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord('a')] += 1
            key = tuple(key)
            dic[key] = dic.get(key, [])
            dic[key].append(word)
        return [v for k, v in dic.items()]


        