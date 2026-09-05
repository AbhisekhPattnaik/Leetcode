class Solution(object):
    def subarraySum(self, nums, k):
        c=0
        sp=0
        sf={0:1}
        for i in nums:
            sp +=i
            c+=sf.get(sp-k,0)
            sf[sp]=sf.get(sp,0)+1
        return c
        