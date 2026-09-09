class Solution(object):
    def countCommas(self, n):
        a=0
        s=1000
        c=1
        while s<=n:
            end=min(n,s*1000-1)
            a+=(end-s+1)*c
            s*=1000
            c+=1
        return a