'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num2 = []
        add = 0
        for i in range(len(nums)):
            add = add+nums[i]
            num2.append(add)
            
        return num2
