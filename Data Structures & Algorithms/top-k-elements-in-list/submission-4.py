class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1 and len(nums) == 1:
            return nums
        
        dic = {}
        
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        arr = []
        for num, cnt in dic.items():
            arr.append([cnt, num])
        arr.sort()
        ret = []
        for j in range(k):
            ret.append(arr.pop()[1])
            
        return ret