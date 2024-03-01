class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)
        res = 0

        res = (nums[i - 1] - 1) * (nums[i - 2] - 1)
        return res
