class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        prev = nums[0]
        longest = 1
        curr = 1
        for idx, i in enumerate(nums[1:]):
            if prev == i:
                prev = i
                continue
            if (i - 1) == prev:
                curr += 1
                prev = i
                if curr > longest:
                    longest = curr
                continue
            curr = 1
            prev = i
        return longest