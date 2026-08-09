class Solution(object):
    def twoSum(self, nums, target):
        hashmap ={}
        for i,num in enumerate(nums):
            c=target-num
            if c in hashmap:
                return [hashmap[c],i]
            hashmap[num] = i      
        