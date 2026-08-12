class Solution(object):
    def singleNumber(self, nums):
        a=set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                a.remove(i)
        return a.pop()
        