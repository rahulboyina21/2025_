class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       idx=self.BS(nums,target,0,len(nums)-1)
       return [-1,-1] if idx==-1 else self.idxs(nums,idx)
    def BS(self,nums: List[int],val:int,start:int,end:int) -> int:
        if(start>end):
            return -1
        mid=start+(end-start)//2
        if(nums[mid]==val):
            return mid
        else:
            if(nums[mid]<val):
                return self.BS(nums,val,mid+1,end)
            else:
                return self.BS(nums,val,start,mid-1)
    def idxs(self,nums: List[int],idx:int):
        leftidx=self.li(nums,0,idx-1,nums[idx])    
        rightidx=self.ri(nums,idx+1,len(nums)-1,nums[idx])
        left = leftidx if leftidx != -1 else idx
        right = rightidx if rightidx != -1 else idx
        return [left, right]

    def li(self,nums,st,ed,val):
        if st>ed:
            return -1
        md=st+(ed-st)//2
        if nums[md]==val:
            ans=self.li(nums,st,md-1,val)
            return md if ans==-1 else ans
        elif nums[md]<val:
            return self.li(nums,md+1,ed,val)
    def ri(self,nums,st,ed,val):
        if st>ed:
            return -1
        md=st+(ed-st)//2
        if nums[md]==val:
            ans=self.ri(nums,md+1,ed,val)
            return md if ans==-1 else ans
        elif nums[md]>val:
            return self.ri(nums,st,md-1,val)








    # def idxs(self,nums: List[int],idx:int):
    #     start,end=0,len(nums)
    #     if end==1:
    #         return [idx,idx]
    #     i,j=idx,idx
    #     val=nums[idx]
    #     iflag,jflag=True,True

    #     while i>=start and j<end:
    #         if(iflag):
    #             if(nums[i]==val):
    #                 if(i==0):
    #                     iflag=False
    #                 else:
    #                     i-=1
    #             else:
    #                 i+=1
    #                 iflag=False        
    #         if(jflag):
    #             if(nums[j]==val):
    #                 if(j==end-1):
    #                     jflag=False
    #                 else:
    #                     j+=1
    #             else:
    #                 j-=1
    #                 jflag=False        
    #         if iflag==False and jflag==False:
    #             return[i,j]
    #         print("i,j = ",i,",",j)
            