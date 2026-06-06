class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ret = nums[0]
        while l <= r:
            m = l + (r - l) // 2
            if nums[l] < nums[r]:
                ret = min(ret, nums[l])
                break

            ret = min(ret, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return ret