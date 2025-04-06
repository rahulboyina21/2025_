class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       idx=self.BS(nums,target,0,len(nums)-1)
       # We are going through each value so we need to give the actual value postion than actual size
       return [-1,-1] if idx==-1 else self.idxs(nums,idx)
       # If there exist no element as such there is no need to find the start and end postion of it so we are going to just return -1 and -1 else we search in either directions
    def BS(self,nums: List[int],val:int,start:int,end:int) -> int:
        if(start>end):
            return -1
        # Basic condition to check we don't end up in a quntaum loop
        mid=start+(end-start)//2
        # finding mid while avoiding the buffer overflow for the integers
        if(nums[mid]==val):
            return mid
            # we found the treasure let's share the postion with the king Ragner sorry Rahul
        else:
            if(nums[mid]<val):
                # we fall behind as per map let's march towards the Russia
                return self.BS(nums,val,mid+1,end)
            else:
                # we went to China let's go back as per map let's march towards the Russia
                return self.BS(nums,val,start,mid-1)
    def idxs(self,nums: List[int],idx:int):
        # Rahul's order's
        # Let me send 2 troop's to find start and end position of the treasure LOL
        # Minions let's do this.
        leftidx=self.li(nums,0,idx-1,nums[idx])
        # From center you go left    
        rightidx=self.ri(nums,idx+1,len(nums)-1,nums[idx])
        # From the center you go right
        left = leftidx if leftidx != -1 else idx
        # If the point of the center is the actual start point then the above will take care by replacing the -1 with the actual idx value you know.
        right = rightidx if rightidx != -1 else idx
        # If the point of the center is the actual start point then the above will take care by replacing the -1 with the actual idx value you know.
        return [left, right]
        # Return the Treasure to the Empror Boyina
    def li(self,nums,st,ed,val):
        if st>ed:
            return -1
        # We avoid the end less quantam hell unlike antman \U0001f41c\U0001f41c\U0001f41c
        md=st+(ed-st)//2
        if nums[md]==val:
            # If we find the treasure in the steps we are taking then we try to take one more step like from the current new point to the boundary of our kingdom not going to the other king's kingdom as King Rahul doesn't want to go to the War this pleasent evening
            ans=self.li(nums,st,md-1,val)
            # Remember in this recursion we are altering the mid value to send it to the next search position but we are also having the orginal mid in place so if we are encountering no more values of treasure also we can be assured we got a point to visit where we got wealth for sure.
            return md if ans==-1 else ans
        elif nums[md]<val:
            # We have reached to the land where is just mud no gold what can we do go back in the direction we came from not taking the lengthy steps we used to came here but one small so that we don;t missout treasure in the any given step
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

# "If I encounter a value greater that the value i am in while going left in the left index then binary search itself could be wrong as I am not stepping in water with both feet so no need to check for the self.li(nums, 0, idx - 1, nums[idx]) while going left and less than while going right"






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
            