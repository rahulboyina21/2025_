class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return False if len(str(sqrt(num)).split('.')[1])>1 else True
        val = isqrt(num)
        return num==val*val