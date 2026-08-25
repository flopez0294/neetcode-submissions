class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, i in enumerate(nums):
            if dic.get(i) is not None:
                return [dic.get(i), idx]
            dic[target - i] = idx
        return []
