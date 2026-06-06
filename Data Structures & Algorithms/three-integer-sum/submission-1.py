class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        
        nums.sort()
        ret = []
        st = set()
        for idx, i in enumerate(nums):
            target = -i
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                if (nums[l] + nums[r] == target):
                    st.add((i, nums[l], nums[r]))
                    l += 1
                elif (nums[l] + nums[r] < target):
                    l += 1
                else:
                    r -= 1

        return list(st)