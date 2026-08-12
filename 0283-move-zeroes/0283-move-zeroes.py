class Solution(object):
    def moveZeroes(self, nums):
        a=[]
        b=[]
        j=0
        k=0
        for i in nums:
            if i==0:
               a.append(i)
            else:
                b.append(i)
        nums[:]=b+a
        return nums