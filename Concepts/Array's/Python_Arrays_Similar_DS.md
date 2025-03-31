# I can say there are 3 main DS for the Array's

1. Arrays themselves from "import array" module
2. Lists which are similar to array but they are kind of dynamic arrays in nature
3. Numpy which is humangasorus of arrays whcih has wide scale of functionality's with easy syntax


## Array's 

``` python
import array as ar

arr_var = ar.array('i'/'f'/'d',[arr1,.........,arrn])

arr_var.insert(1 'pos',4 'val')

arr_var.pop(index) / arr_var.pop() -> removes the last element

arr_var.remove(value) // Removes that particular value from the array

# Unpacking array's and print them using the * infront of the array variable like *arr

```

## Lists 

``` Python Lists
li = [1,2,3,4,5,a,b,c,d,{a:b}] // Yeah it's mixed vegitable curry lol

li.append(1)

li.insert(0,0) // insert at 0 index value 0.

li.pop() // Removes the last element.

li.remove(value) // Removes that particular value's first occurance from the list.

li.extend([1,2,3,4,5])

li.index(value) // Returns the index of that particular value

li.count(value) // Return the count of the value that has occured in the given list

li.sort(li)

li.reverse(li)

li_copy=li.copy()

li.clear()

```


## Numpy 

### They are beast's for numerical operations imagine you want to do something with the numbers some scitenfic operations then this is the goto

``` python numpy

  import numpy as np

arr = np.array([1,2,3,4,5])

arr.zeros((rows,columns))

arr.ones((rows,columns))

// Random Number generation methods

arr.arange(0,100,0.5) // Start, Stop, Step_Size // to step according to the given space 

arr.linspace=(start,stop,num=number of elements that are needed in a evenly spaced manner) // distribute the given space in points it will multiply

// Element wise operations

arr+2 // all the elements will be added with 2

arr-2 // all the elements will be dedcuted with 2

// Basic Operations

arr.sum()

arr.mean()

arr.min()

arr.max()

// Matrix

we can perform element to element operations just like that but if we want to multiply there we need to be catious

// Matrix multiplication has syntx as mat1 @ mat2

// 2 ways to multiply

prod= mat1 @ mat2

prod = np.dot(mat1,mat2)

// Manipulating the structure of the matrix

considering the total number of elements we can manipulate them to fit in a Row x Column = Same number of values

rs = arr.reshape(2,3) // Row,Columns

// Transpose

at = rs.T

// Filtering Operations

arr = arr[condtion]

arr[condition] = Value to be updated for the condition

ex:

arr = arr[arr >/</>=/<= value] here each value is measured for that particular iteration of that element

arr[arr >/</>=/<= value] = New Value // Here for the each element in the array satisies the given ondtion the new element will be updated with.

```


### All methods summerized 

## Common Methods: Lists vs. Arrays vs. NumPy

| **Method**       | **Python List**  | **Array Module** (`array.array`) | **NumPy Array** (`np.array`) |
|-----------------|----------------|---------------------|---------------------|
| **Access Elements (`arr[i]`)** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Append (`append(x)`)** | ✅ `list.append(x)` | ✅ `arr.append(x)` | ❌ Use `np.append(arr, x)` |
| **Insert (`insert(i, x)`)** | ✅ `list.insert(i, x)` | ❌ No direct method | ❌ Use `np.insert(arr, i, x)` |
| **Extend (`extend(iterable)`)** | ✅ `list.extend([...])` | ❌ No direct method | ❌ Use `np.concatenate((arr1, arr2))` |
| **Remove by Value (`remove(x)`)** | ✅ `list.remove(x)` | ❌ No direct method | ❌ Use `arr[arr != x]` or `np.delete()` |
| **Remove by Index (`pop(i)`)** | ✅ `list.pop(i)` | ❌ No direct method | ❌ Use `np.delete(arr, i)` |
| **Sort (`sort()`)** | ✅ `list.sort()` (modifies in place) | ❌ No direct method | ✅ `np.sort(arr)` (returns new array) |
| **Reverse (`reverse()`)** | ✅ `list.reverse()` | ❌ No direct method | ✅ `arr[::-1]` (slicing) |
| **Index (`index(x)`)** | ✅ `list.index(x)` | ❌ No direct method | ✅ `np.where(arr == x)` |
| **Count (`count(x)`)** | ✅ `list.count(x)` | ❌ No direct method | ✅ `np.count_nonzero(arr == x)` |
| **Length (`len(arr)`)** | ✅ `len(list)` | ✅ `len(arr)` | ✅ `arr.size` or `len(arr)` |
| **Sum (`sum(arr)`)** | ✅ `sum(list)` | ❌ No direct method | ✅ `np.sum(arr)` |
| **Min (`min(arr)`)** | ✅ `min(list)` | ❌ No direct method | ✅ `np.min(arr)` |
| **Max (`max(arr)`)** | ✅ `max(list)` | ❌ No direct method | ✅ `np.max(arr)` |
| **Copy (`copy()`)** | ✅ `list.copy()` | ❌ No direct method | ✅ `arr.copy()` |
| **Clear (`clear()`)** | ✅ `list.clear()` | ❌ No direct method | ❌ Use `arr[:] = 0` or `arr.fill(0)` |
| **Slicing (`arr[start:stop:step]`)** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Mathematical Operations (`+`, `-`, `*`, `/`)** | ❌ No (requires loops) | ❌ No | ✅ Yes (Vectorized) |
| **Reshape (`reshape()`)** | ❌ No | ❌ No | ✅ `arr.reshape(rows, cols)` |
| **Transpose (`T`)** | ❌ No | ❌ No | ✅ `arr.T` |
| **Filtering (`arr[arr > x]`)** | ❌ No | ❌ No | ✅ Yes |


### Why Some Methods are missing in other DS 

## Why Some Methods Are Missing in Lists, Arrays, and NumPy

- **append()**  
  - ✅ List: Supports dynamic resizing.  
  - ✅ `array.array`: Supports fixed-type but can grow.  
  - ❌ NumPy: Arrays are **fixed-size**, so `np.append()` creates a new array.

- **insert()**  
  - ✅ List: Allows dynamic insertion.  
  - ❌ `array.array`: No built-in method for insertion.  
  - ❌ NumPy: Arrays have **fixed memory layout**, so `np.insert()` returns a new array.

- **extend()**  
  - ✅ List: Can hold mixed types, allows direct extension.  
  - ❌ `array.array`: No built-in method; must append individually.  
  - ❌ NumPy: Only allows **same-type arrays**, so `np.concatenate()` is used.

- **remove(element)**  
  - ✅ List: Searches and removes the first occurrence.  
  - ❌ `array.array`: No built-in method; must be done manually.  
  - ❌ NumPy: Arrays are **optimized for bulk operations**, so filtering (`arr[arr != x]`) is used.

- **pop(index)**  
  - ✅ List: Removes and returns an element.  
  - ❌ `array.array`: No built-in method for removing by index.  
  - ❌ NumPy: Arrays have **fixed size**, so `np.delete()` creates a new array.

- **sort()**  
  - ✅ List: Sorts elements in place.  
  - ❌ `array.array`: No built-in method; must use `sorted()`.  
  - ✅ NumPy: Uses `np.sort()` but returns a **new sorted array**.

- **reverse()**  
  - ✅ List: Can reverse in place.  
  - ❌ `array.array`: No built-in method for reversing.  
  - ✅ NumPy: Uses slicing (`arr[::-1]`) for reversal.

- **index(x)**  
  - ✅ List: Finds first occurrence.  
  - ❌ `array.array`: No built-in method for searching.  
  - ✅ NumPy: Uses `np.where()` to locate indices.

- **count(x)**  
  - ✅ List: Counts occurrences of an element.  
  - ❌ `array.array`: No built-in method; requires iteration.  
  - ✅ NumPy: Uses `np.count_nonzero(arr == x)` for fast counting.

- **clear()**  
  - ✅ List: Removes all elements.  
  - ❌ `array.array`: No direct method; must create a new empty array.  
  - ❌ NumPy: Must use `arr[:] = 0` or `arr.fill(0)` (can't resize in place).

- **Mathematical operations (`+`, `-`, `*`, `/`)**  
  - ❌ List: Requires loops or list comprehensions.  
  - ❌ `array.array`: No built-in support for element-wise operations.  
  - ✅ NumPy: Supports **vectorized operations**, making it much faster.

- **reshape()**  
  - ❌ List: No built-in multi-dimensional support.  
  - ❌ `array.array`: Only supports 1D data.  
  - ✅ NumPy: Uses `arr.reshape(rows, cols)` for reshaping.

- **transpose()**  
  - ❌ List: No concept of transposing.  
  - ❌ `array.array`: Only supports 1D data.  
  - ✅ NumPy: Uses `arr.T` to swap rows and columns.

- **Filtering (`arr[arr > x]`)**  
  - ❌ List: Requires list comprehensions.  
  - ❌ `array.array`: No built-in filtering mechanism.  
  - ✅ NumPy: Supports **fast element-wise filtering** using conditions.
 

### Key Takeaways
- Lists are dynamic and support flexible operations.
- `array.array` is type-restricted and lacks many built-in methods.
- NumPy arrays are fixed-size but optimized for numerical computations.
- ❌ `array.array`: No built-in method for insertion (**must convert to list first**).
