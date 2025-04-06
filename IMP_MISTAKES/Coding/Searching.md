# You should Make a mistak only once and never again

## LOL Mistakes
<details open>
<summary><strong>All Mighty BS -> Sorry -> Binary Search</strong></summary>
<br>
  
``` Python BS

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
        i,j=idx,idx
        val=nums[idx]
        iflag,jflag=True,True

        while i>=start and j<end:
            if(iflag):
                if(nums[i]==val):
                    i-=1
                else:
                    i+=1
                    iflag=False        
            if(jflag):
                if(nums[j]==val):
                    j+=1
                else:
                    j-=1
                    jflag=False        
            if iflag==False and jflag==False:
                return[i,j]

```

#### Observations 
1. What if there is only single element in the search space then our coding concept to iterate over the element brutally fails as we will set i=-1 and j=1 both will stop the while loop and we are left with sand in the jar [-1,-1] sorry sand also doesn't exist in our desert as we returning null noooooo not even null -> None exist which is a void space that is not even nothing like we can if there is nothing we can nothing here there could be something or nothing so welcome to ant man's quantum realm why i am going there stick to the topic RAHUL let's go.
```python
    def idxs(self,nums: List[int],idx:int):
        start,end=0,len(nums)
        if end==1:
            return [idx,idx]
```
the above code should our issue but guess what we got another one ... !
why why why why godddddddddd ... !
i got this let me do it.
2. New error for the test case [2,2] and target is 2 it is failing but why let's observe.
  1. My observation is we are facing problemw with the extreme edges like first or last when we hit the wall we don't have go beyond it so let's check for it problem solved Simple REALLY the code now looks like spagathee bowl with the chinese chilli sauce all over it now wanna add bit more spice to it Yeah!!!!!!!!!!!!!!!!!!!!!!!!.
``` python

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

```

Hurrah i have successfully debugged it and submitted the code 
Really RAHUL what's it's stat's 
![image](https://github.com/user-attachments/assets/e3c857d7-7ca1-497c-8d19-e46ba23661a3)
Yoooooooooo my grandma run's faster than your python code 
![image](https://github.com/user-attachments/assets/c192bab7-a921-4501-b877-a18d4b346ab9)
That's it let me optimize the code

Check list:
Binary Search Logic -> It's Crisp no need to furthur optimize.
Linear Search logic is not so optimal if whole array is of one element duplicated for 10**5 then inital binary search went into the vein.
i can convert this linear search into the two parts 
1. Use 1 binary search to move towards left and other towards the right it is the best optimization you can do on this.
2. eliminate the issue of complex if-else mess -> remember no more than 2 depths for optimial code redabilty

let's write the algo first 

1. when we are moving in the direction of the right to left we need to make sure of few thing.
   in Binary Search i always imagine a biscut and i make it equal half of each half every time thus it goes into the n*log n complexity
  1. Now we need to make sure when breaking we break in the given boundary's if we encounter any boundary which is of not in the specified limit then we hold on to the correct boundary and change the incorrect boundary.
![image](https://github.com/user-attachments/assets/54a4ff40-02bc-4745-b09f-1c7bd99b9314)

2. Same goes for the left to the right as well.
![image](https://github.com/user-attachments/assets/8ea7ee8f-c61d-41b3-b1c0-7c06e0896345)

Hole of the Logic 

![image](https://github.com/user-attachments/assets/a869b38b-a691-4711-9e94-db112499c0ec)

``` python left

def li(self,nums,st,ed,val):
        if st>ed:
            return -1
        # We avoid the end less quantam hell unlike antman 🐜🐜🐜
        md=st+(ed-st)//2
        if nums[md]==val:
            # If we find the treasure in the steps we are taking then we try to take one more step like from the current new point to the boundary of our kingdom not going to the other king's kingdom as King Rahul doesn't want to go to the War this pleasent evening
            ans=self.li(nums,st,md-1,val)
            # Remember in this recursion we are altering the mid value to send it to the next search position but we are also having the orginal mid in place so if we are encountering no more values of treasure also we can be assured we got a point to visit where we got wealth for sure.
            return md if ans==-1 else ans
        elif nums[md]<val:
            # We have reached to the land where is just mud no gold what can we do go back in the direction we came from not taking the lengthy steps we used to came here but one small so that we don;t missout treasure in the any given step
            return self.li(nums,md+1,ed,val):


```

``` python right

def ri(self,nums,st,ed,val):
        if st>ed:
            return -1
        md=st+(ed-st)//2
        if nums[md]==val:
            ans=self.ri(nums,md+1,ed,val)
            return md if ans==-1 else ans
        elif nums[md]>val:
            return self.ri(nums,st,md-1,val)


```

``` python Big hole code

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
        # We avoid the end less quantam hell unlike antman 🐜🐜🐜
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



```

### Conqured the Title the best time complexity title goes to the all mighty undisputed Rockyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
![image](https://github.com/user-attachments/assets/fa75f0dd-b691-4ed4-af25-499eee9644d5)
![image](https://github.com/user-attachments/assets/b1962667-da68-47a2-b42a-a51f067f7e89)


![image](https://github.com/user-attachments/assets/3a5495fd-0d13-4f20-b0ee-c913c7908b0c)


</details>
