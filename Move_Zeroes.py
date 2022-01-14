'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n,j = len(nums), 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[j] = nums[i]
                j+=1
        while(j<n):
            nums[j] = 0
            j+=1
           
           
           '''
           n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[n] = nums[n], nums[i]
                n += 1
           '''
           
           
           
