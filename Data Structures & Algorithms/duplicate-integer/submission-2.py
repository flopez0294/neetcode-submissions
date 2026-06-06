class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2: 
            return False
        nums.sort()
        prev = nums[0]
        for i in nums[1:]:
            if prev == i:
                return True
            prev = i

        return False
        