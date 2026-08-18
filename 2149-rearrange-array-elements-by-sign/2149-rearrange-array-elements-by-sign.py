class Solution(object):
    def rearrangeArray(self, nums):
        a=[]
        b=[]
        k=0
        l=0
        m=0
        for i in nums:
            if i>0:
                a.append(i)
            else:
                b.append(i)
        c=[0]*len(nums)
        while l<len(a) and m<len(b):
            if a[l]>0:
                c[k]=a[l]
                l+=1
                k+=1
                c[k]=b[m]
                m+=1
                k+=1
        return c

        