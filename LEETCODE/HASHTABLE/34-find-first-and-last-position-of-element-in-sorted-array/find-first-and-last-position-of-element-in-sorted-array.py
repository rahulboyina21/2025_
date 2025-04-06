class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       idx=self.BS(nums,target,0,len(nums)-1)
       if idx==-1:
        return [-1,-1]
       return self.idxs(nums,idx)
    def BS(self,nums: List[int],val:int,start:int,end:int) -> int:
        if(start>end):
            print("no mid")
            return -1
        mid=start+(end-start)//2
        if(nums[mid]==val):
            print("Mid = ",mid)
            return mid
        else:
            if(nums[mid]<val):
                return self.BS(nums,val,mid+1,end)
            else:
                return self.BS(nums,val,start,mid-1)
    def idxs(self,nums: List[int],idx:int):
        start,end=0,len(nums)
        if end==1:
            return [idx,idx]
        i,j=idx,idx
        val=nums[idx]
        iflag,jflag=True,True

        while i>=start and j<end:
            if(iflag):
                if(nums[i]==val):
                    if(i==0):
                        iflag=False
                    else:
                        i-=1
                else:
                    i+=1
                    iflag=False        
            if(jflag):
                if(nums[j]==val):
                    if(j==end-1):
                        jflag=False
                    else:
                        j+=1
                else:
                    j-=1
                    jflag=False        
            if iflag==False and jflag==False:
                return[i,j]
            print("i,j = ",i,",",j)
            