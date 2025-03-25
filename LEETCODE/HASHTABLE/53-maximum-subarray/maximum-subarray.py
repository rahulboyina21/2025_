class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsum,csum=-float('inf'),0
        size=len(nums)
        if size==1:
            return nums[0]
        for i in range(size):
            if csum<0:
                csum=0
            csum+=nums[i]
            mxsum=max(mxsum,csum)
        
        return mxsum
        