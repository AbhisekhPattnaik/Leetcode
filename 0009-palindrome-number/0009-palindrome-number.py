class Solution(object):
    def isPalindrome(self, x):
        o=x
        rev=0
        if x < 0:
            return False
        else:
            while x>0:

             pal=x%10
             rev=rev*10+pal
             x= x//10
            return o==rev
            
        