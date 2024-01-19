# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%(len(nums))
        if k>0:
            nums.reverse()
            nums[:k]=nums[:k][::-1]
            nums[k:]=nums[k:][::-1]
