class Solution(object):
    def isValid(self, s):
        stack=[]
        pair= {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for i in s:
            if i in pair:
                if not stack or stack[-1]!= pair[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0

        