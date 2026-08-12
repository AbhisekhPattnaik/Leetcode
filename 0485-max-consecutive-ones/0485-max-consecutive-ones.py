class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        cm=0
        for i in nums:
            if i==1 and i!=0:
                c+=1
                if cm<=c:
                    cm=c
            elif i==0 :
                c=0
        return cm


        