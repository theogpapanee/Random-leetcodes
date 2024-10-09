# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2024-10-09
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        b = 0
        c = 0
        for i in s:
            if i == '(':
                a+=1
            elif b >= a:
                c+=1
            else:
                b+=1
        return abs(a-b) + c
        
        
