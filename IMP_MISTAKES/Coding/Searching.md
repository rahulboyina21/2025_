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

def(self,nums,val,st,ed):


```

``` python right

def(self,nums,val,st,ed):


```

</details>
