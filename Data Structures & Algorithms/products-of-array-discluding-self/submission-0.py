class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for idx, i in enumerate(nums[1:]):
            prefix.append(prefix[idx] * nums[idx])
        suffix = [1]
        for idx, i in enumerate(nums[-2::-1]):
            suffix.append(suffix[idx] * nums[len(nums) - 1 - idx])

        leng = len(suffix)
        suffix[::-1]
        for idx, i in enumerate(prefix):
            nums[idx] = i * suffix[leng - idx - 1]
        return nums