"""Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        start = 0
        end = len(s)-1
        while(start<end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start+=1
            end-=1
        
        #s.reverse()
        
        #s[:] = s[::-1]
