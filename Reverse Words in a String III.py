'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        l=""
        count=0
        for x in s.split():
            count+=1
        for x in s.split():
            l+=x[::-1]
            if(count>1):
                l+=" "
                count-=1
        return l
      
      
      #return " ".join([word[::-1] for word in s.split()])
