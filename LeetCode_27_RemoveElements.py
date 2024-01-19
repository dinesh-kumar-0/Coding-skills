#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur_pos = 1
        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[cur_pos] = nums[i]
                cur_pos += 1
        return cur_pos
