class Solution(object):
    def check(self, nums):
        c=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1
        if c==0:
            return True
        elif c==1 and nums[-1]<=nums[0]:
            return True
        else:
            return False        
        