class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            return 0 if nums[0]>target else 1
        return self.BS(nums,target,0,len(nums)-1)
    def BS(self,nums: List[int],val: int,st:int,ed:int)-> int:
        if(st>ed):
            return st
        else:
            md=st+(ed-st)//2
            if nums[md]==val:
                return md
            elif nums[md]<val:
                ans=self.BS(nums,val,md+1,ed)
                # if ans==-1:
                #     if nums[md]<val:
                #         ans=md+1
                #     elif md!=0:
                #         ans=md-1
                #     else:
                #         ans=0
                return ans
            else:
                ans=self.BS(nums,val,st,md-1)
                # if ans==-1:
                #     if nums[md]>val:
                #         ans=md-1
                #     elif md!=0:
                #         ans=md-1
                #     else:
                #         ans=len(nums)
                return ans