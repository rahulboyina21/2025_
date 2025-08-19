class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        for i in s:
            if i.isalnum()==True:
                ans+=i
        # print(ans," ","".join(reversed(ans)))
        if ans == "".join(reversed(ans)):
            return True
        return False