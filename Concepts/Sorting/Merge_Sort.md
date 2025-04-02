# Merge Sort

**As the name suggest we are going to merge to get the sorted array/list/ any linear data structure**

- Questions
- What are we going to merge ?
- what is the motive of this algo like hidden mechanism
- Is this the best we got ?

1. Firstly think of it like a given array is being broken into atomic size at end by breaking into even pieces in each move like below.

![image](https://github.com/user-attachments/assets/ae1a427c-3ee4-4f44-b154-dac13912e1eb)

2. Then we are going to move them into the merge function where we recursively solve the given atomic value by sorting them and combing them into one.
3. merge function will accept 3 arguments
   1. left sub array
   2. right sub array
   3. orginal array from which these values broken from.

**The Merging happens as below**

![image](https://github.com/user-attachments/assets/bdcebcb5-1a2d-4d8c-af76-34f0531f28bf)

**Complexity**

*Time Complexity*
![image](https://github.com/user-attachments/assets/1d6fa649-653a-46e7-bbbe-02e3f8b97a61)

*Space Complexity*
![image](https://github.com/user-attachments/assets/9e7717bd-75fc-4297-bd5f-6f8ae145e081)

## Summery
**How it works:**
1.Divide the unsorted array into two sub-arrays, half the size of the original.
2.Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
3.Merge two sub-arrays together by always putting the lowest value first.
4.Keep merging until there are no sub-arrays left.

![img_mergesort_long](https://github.com/user-attachments/assets/c7147d68-20cc-4bb9-adbc-265f7b3c656e)

``` python merge sort


def splitter(arr):
    size=len(arr)
    if size==1:
        return arr
    mid=size//2
    
    sorted_left_array=splitter(arr[:mid])
    sorted_right_array=splitter(arr[mid:])
    
    return merger(sorted_left_array,sorted_right_array)


def merger(lar,rar):
    res=[]
    llen,rlen,i,j=len(lar),len(rar),0,0
    
    while i<llen and j<rlen:
        if lar[i]<rar[j]:
            res.append(lar[i])
            i+=1
        else:
            res.append(rar[j])
            j+=1
    res.extend(lar[i:])
    res.extend(rar[j:])
    return res

number=[
    847, 92, 634, 719, 300, 419, 221, 982, 571, 154,
    730, 408, 53, 246, 997, 358, 783, 167, 401, 998,
    284, 648, 356, 201, 679, 39, 472, 810, 133, 624,
    95, 10, 754, 812, 666, 148, 500, 443, 228, 312,
    905, 798, 223, 122, 431, 366, 37, 61, 186, 799,
    620, 44, 962, 780, 995, 142, 273, 19, 841, 106,
    808, 871, 290, 216, 330, 421, 252, 488, 71, 687,
    278, 33, 60, 545, 84, 634, 501, 38, 777, 873,
    251, 379, 200, 932, 356, 189, 608, 961, 745, 820,
    505, 920, 309, 777, 435, 604, 132, 888, 440, 579
]


number=splitter(number)

print(number)


```

