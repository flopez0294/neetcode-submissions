class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            key = [0] * 26
            for ch in i:
                key[ord(ch) - ord('a')] += 1
            dic[tuple(key)].append(i)
        return list(dic.values())