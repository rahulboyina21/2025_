class Solution:
    def BS(self,nums,val,l,h):
        if l>h:
            return -1
        else:
            m = l+(h-l)//2
            if nums[m]==val:
                return m
            
            if nums[m]<val:
                return self.BS(nums,val,m+1,h)
            else:
                return self.BS(nums,val,l,m-1)

    def search(self, nums: List[int], target: int) -> int:
        return self.BS(nums,target,0,len(nums)-1)
    
    
