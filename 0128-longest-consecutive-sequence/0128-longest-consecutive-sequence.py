class Solution(object):
    def longestConsecutive(self, nums):
        num_set=set(nums)
        l=0
        for num in num_set:
            if num-1 not in num_set:
                c=num
                len=1
                while c+1 in num_set:
                    c+=1
                    len+=1
                l=max(l,len)
        return l