class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for i in t:
            if dic.get(i,0) <= 0:
                return False
            dic[i]=dic.get(i,0)-1
        for k,v in dic.items():
            if v>=1:
                return False
        return True