class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1 and len(nums) == 1:
            return nums
        
        dic = {}
        
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        dic = dic.items()
        dic = sorted(dic, key = lambda x:x[1])
        ret = []
        for j in range(k):
            ret.append(dic.pop()[0])
            
        return ret