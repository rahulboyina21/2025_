# Quick Sort -> Everything in one page

| **Partition Scheme**         | **Pivot Selection**                   | **When to Use**                                | **Key Characteristics**                                                                 |
|------------------------------|---------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------|
| Lomuto Partition Scheme      | Typically last element                | Simple to implement, good for learning         | Scans left to right; not efficient for duplicate-heavy or sorted arrays.                 |
| Hoare Partition Scheme       | Typically middle or random element    | Better average-case performance than Lomuto    | Fewer swaps; more efficient; harder to implement correctly.                             |
| Randomized Quick Sort        | Random element                        | When input distribution is unknown             | Reduces chance of worst-case; better average performance.                                |
| Median-of-Three Partition    | Median of first, middle, and last     | When array might be partially sorted           | Reduces chances of worst-case time; simple heuristic improvement.                        |
| Dual-Pivot Quick Sort        | Two pivots (e.g., first and last)     | Used in Java's Arrays.sort() for primitives    | Divides into three parts; faster in practice for large datasets.                         |
| Dutch National Flag (3-Way)  | Chosen pivot (any method)             | When array has many duplicate elements         | Splits array into <pivot, =pivot, >pivot; very efficient with repeated values.           |


**why but why ?**

- ## You will know at the end follow along lol
1. Similar to many algorithms the core goal is to sort that is so obvious as by the name what all concepts are used in this
  1. Pivot - It can start / end / middle but mostly the end is used as a pivot.
    - we need to find the final resting spot of this pivot
  2. the concept around the pivots are the major aspect that would dtermine how good our algorithm is working like imagine taking your algo from O(n**2) to just O(nlogn)
     Kinds of pivot selection methods we can consider are
     1. Lomuto partition scheme -> In this very scheme we will cosnider the last element as the pivot element and will be moving every element less than that element to the left side of that pivot element and greater than equal to elements to the right side of the pivot that's how segreation works imagine the last element is the least or greatest element then we will have O(n**2) for sure that's inevidable LOL.

``` Python Quick Sort
def QS(arr):
    size = len(arr)
    if size<=1:
        return arr
    pivot=arr.pop()
    
    lsa,rsa=[],[]
    
    for i in arr:
        if i<pivot:
            lsa.append(i)
        else:
            rsa.append(i)
    
    return QS(lsa)+[pivot]+QS(rsa)
test_list = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498,
             415, 941, 803, 850, 311, 664, 877, 672, 613, 152,
             748, 289, 90, 691, 856, 90, 759, 48, 339, 153,
             123, 992, 132, 642, 304, 56, 787, 763, 936, 727,
             558, 738, 740, 74, 296, 460, 290, 35, 361, 532,
             210, 205, 369, 45, 557, 649, 629, 386, 157, 63,
             975, 637, 82, 220, 113, 924, 740, 840, 613, 255,
             185, 218, 858, 578, 46, 447, 56, 662, 369, 588,
             974, 75, 396, 773, 303, 153, 697, 236, 665, 894,
             598, 830, 913, 738, 939, 926, 823, 166, 46, 994]
print(QS(test_list))

# print(test_list)

```

## The above code is the a sorting method variation of the quick sort where we are not using the inplace sorting where we are using the extra space for the left and right subarray-s which would be an expensive operation when we are using a very large size array's or sequence the best way to get started is to understand it's mechanism's now we can improve one step a time ain't no need to aim for the optimal solution in the first throw just focus on proceeding by gradual improvement's


### Question is what can be improved ?
1. The memory is what can be improved if we are using the extra space as much as the size of the array and we incrementally go down by it's minature version in each iteration it's way expensive. Sol -> go for the inplace sorting simple and effective solution Lov.
2. There are few simple adjestments can be done to the process like checking the pivot element.


``` Python Quick Sort Not Inplace
def QS(arr):
    size = len(arr)
    if size<=1:
        return arr
    pivot=arr.pop()
    
    lsa,rsa=[],[]
    
    for i in arr:
        if i<pivot:
            lsa.append(i)
        else:
            rsa.append(i)
    
    return QS(lsa)+[pivot]+QS(rsa)
```



``` Python Quick Sort Inplace - Lomuto Schema

def QS(arr,low,high):
    # Lomuto Schema last element as pivot
    
    if low>=high:
        return arr
    else:
        pivot = arr[high]
        
        j=low 
        # J will act as a switch to flip and swap the high values with low values
        
        for i in range(low,high):
            if(arr[i]<=pivot):
                arr[j],arr[i]=arr[i],arr[j]
                j+=1
                # Right value is under j so that value is under pivot so we increment the j
        
        arr[j],arr[high]=arr[high],arr[j]
        
        # J acts as a division between 2 ranges of values but these values are not in order
        # for which we need to apply the sort once again
        
        QS(arr,low,j-1)
        QS(arr,j+1,high)
            
    
    
test_list = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498,
             415, 941, 803, 850, 311, 664, 877, 672, 613, 152,
             748, 289, 90, 691, 856, 90, 759, 48, 339, 153,
             123, 992, 132, 642, 304, 56, 787, 763, 936, 727,
             558, 738, 740, 74, 296, 460, 290, 35, 361, 532,
             210, 205, 369, 45, 557, 649, 629, 386, 157, 63,
             975, 637, 82, 220, 113, 924, 740, 840, 613, 255,
             185, 218, 858, 578, 46, 447, 56, 662, 369, 588,
             974, 75, 396, 773, 303, 153, 697, 236, 665, 894,
             598, 830, 913, 738, 939, 926, 823, 166, 46, 994]
QS(test_list,0,len(test_list)-1)

print(test_list)

```

## Explination

![image](https://github.com/user-attachments/assets/5ca18bfd-457c-427d-bb5b-99932fddce37)


# Hoare Parition Schema

## Hoare Partition Scheme – Verbal Algorithm

1. **Choose the pivot**  
   - Take the **first element** of the array as the pivot.

2. **Initialize pointers**  
   - Set `i = low - 1`  
   - Set `j = high + 1`

3. **Start infinite loop**
   - Repeat the following steps:

   a. Move `i` forward:  
      - Keep increasing `i` until `arr[i] ≥ pivot`.

   b. Move `j` backward:  
      - Keep decreasing `j` until `arr[j] ≤ pivot`.

   c. **If `i ≥ j`**,  
      - Return `j` (this is the partition index).

   d. **Else**,  
      - Swap `arr[i]` and `arr[j]`.

4. **Continue** the loop until `i ≥ j`.

# All of the concept and code 

![20250403_175019](https://github.com/user-attachments/assets/02328fe2-c3b1-4e5b-8890-65e73c7d51a2)


``` Python Hoare Algo Code
def QS(arr,low,high):
    # Lomuto Schema last element as pivot
    
    if low>=high:
        return arr
    else:
        pivot = arr[low]
        i=low-1
        j=high+1
        
        while True:
            
            while True:
                i+=1
                if arr[i]>=pivot:
                    break
            
            while True:
                j-=1
                if arr[j]<=pivot:
                    break
            
            if i>=j:
                break
            arr[i],arr[j]=arr[j],arr[i]
            
        
        QS(arr,low,j)
        QS(arr,j+1,high)
            
    
    
test_list = [865, 395, 777, 912, 431, 42, 266, 989, 524, 498,
             415, 941, 803, 850, 311, 664, 877, 672, 613, 152,
             748, 289, 90, 691, 856, 90, 759, 48, 339, 153,
             123, 992, 132, 642, 304, 56, 787, 763, 936, 727,
             558, 738, 740, 74, 296, 460, 290, 35, 361, 532,
             210, 205, 369, 45, 557, 649, 629, 386, 157, 63,
             975, 637, 82, 220, 113, 924, 740, 840, 613, 255,
             185, 218, 858, 578, 46, 447, 56, 662, 369, 588,
             974, 75, 396, 773, 303, 153, 697, 236, 665, 894,
             598, 830, 913, 738, 939, 926, 823, 166, 46, 994]
QS(test_list,0,len(test_list)-1)

print(test_list)

```


## 🧠 Hoare Partition – Recap Summary

- ✅ **Pivot Selection**  
  - Always pick `arr[low]` as the pivot in Hoare’s scheme.

- ✅ **Initial Pointers**  
  - Set `i = low - 1`, `j = high + 1`

- 🔁 **Loop Behavior**  
  - `i` moves **right** until `arr[i] >= pivot`  
  - `j` moves **left** until `arr[j] <= pivot`

- ❗ **Check `i >= j` before swap**  
  - If `i >= j`, return `j`  
  - Do **not** swap after pointers cross

- 🔁 **Swap only if `i < j`**  
  - Swap `arr[i]` and `arr[j]` before crossing

- ✅ **No need to place pivot at final position**  
  - Hoare’s scheme **does not** place pivot in the middle at the end

- 🔥 **Why `i = low - 1` works best**  
  - Allows `i += 1` before checking `arr[i]`  
  - Handles edge cases (e.g., pivot at index 0)

- 🚫 **Why `i = low` version can fail**  
  - If `arr[j]` is accessed **before** `j -= 1`, may cause **IndexError**  
  - Fails when all elements are `< pivot` → `j` can go to `-1`

- ✅ **Classic version is safer**  
  - Checks happen **after moving** pointers  
  - Prevents out-of-bound access and runtime errors

- 💡 **How to use in QuickSort**:
  ```python
  p = hoare_partition(arr, low, high)
  quicksort(arr, low, p)
  quicksort(arr, p + 1, high)
  ```
### ⚠️ Important Point – Why `quicksort(arr, low, j)` is Correct in Hoare Partition

- ✅ In **Hoare's partition**, the returned `j` is the **final index of the left partition**.
- ✅ So we must include it in the next recursive call:  
  `quicksort(arr, low, j)`

- ❌ If you do `quicksort(arr, low, j - 1)`, you:
  - Might **skip sorting index `j`**
  - Could cause **incomplete sorting**
  - Risk **infinite recursion** when `low == j`

- 💡 Always use:
  ```python
  quicksort(arr, low, j)
  quicksort(arr, j + 1, high)
  ```

  ### ⚠️ Important Point – Don't Mix Hoare and Lomuto

- ❗ Do **not** mix Hoare logic with Lomuto pivot selection.
- Decide between one of the two:

- ✅ **Hoare Partition**
  - Use: `pivot = arr[low]`
  - Method: Two-pointer `i` and `j` with infinite `while` loop
  - Swap when `i < j`, stop when `i >= j`

- ✅ **Lomuto Partition**
  - Use: `pivot = arr[high]`
  - Method: Single scan using `i` and `j` in a `for` loop
  - Final swap places pivot at correct index

- 🔥 Mixing pivot of Lomuto (`arr[high]`) with Hoare's logic will lead to incorrect results or runtime errors.
  
