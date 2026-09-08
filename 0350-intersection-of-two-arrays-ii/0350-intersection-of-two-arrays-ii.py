class Solution(object):
    def intersect(self, nums1, nums2):
        ls=[]
        for i in nums1:
         if i in nums2:
             ls.append(i)
        r=[]
        for i in ls:
            if i not in r:
                c1=nums1.count(i)
                c2=nums2.count(i) 
                m=min(c1,c2)   
                for j in range(m):
                    r.append(i)
        return r    
        
        