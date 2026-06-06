class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]

        space = {}
        for i in range(len(nums)):
            j = space.get(nums[i])
            if j is not None:
                return [j, i]
            diff = target - nums[i]
            space[diff] = i;
        return []