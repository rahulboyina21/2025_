# Binary Search

1. It's a search Algo of the sorted element's.
2. we need to find the mid element which is (low + high)//2 Welcome to integer overflow for big values so we need to use this formulae low + (high - low)/2 to avoid overflow.
3. now we need to check if mid point value is < or > or = to our value
   1. If < then we need to move forward so low will be set as Low = Mid + 1 and High = Len(arr)-1
   2. if > then we can far ahead need to go back so we will exclude furthur search space and set Low = 0 and High = Mid -1
   3. if = then congrats Bruh so you got a jackpot saved ton of iteration return the Index and sleep it's getting late LOL.
   4. if you went to the last element and you can't find the element lol no worries just return -1.

``` Python Binary Search

def BS(arr,val,low,high):
    
    if low>high:
        return -1
        
    mid = low + (high-low)//2
    
    if arr[mid]==val:
        return mid
    
    
    if arr[mid]<val:
        return BS(arr,val,mid+1,high)
        
    else:
        return BS(arr,val,low,mid-1)
    
    
arr = [1, 3, 5, 7, 9, 11]
print(BS(arr, 7, 0, len(arr) - 1))  
print(BS(arr, 4, 0, len(arr) - 1))  

```

# 📊 Binary Search Problem Tier List with Real Examples

---

## 🟢 Basic / Easy

| Problem | Platform |
|--------|----------|
| Find element in sorted array | [LeetCode 704](https://leetcode.com/problems/binary-search/) |
| [First and Last Occurrence](https://github.com/rahulboyina21/2025_/blob/main/IMP_MISTAKES/Coding/Searching.md#you-should-make-a-mistak-only-once-and-never-again) | [LeetCode 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| Count of occurrences | GFG: Count Occurrences |
| Square root (floor) | [LeetCode 69](https://leetcode.com/problems/sqrtx/) |
| Search Insert Position | [LeetCode 35](https://leetcode.com/problems/search-insert-position/) |
| Is number a perfect square | [LeetCode 367](https://leetcode.com/problems/valid-perfect-square/) |

---

## 🟡 Moderate

| Problem | Platform |
|--------|----------|
| Binary Search on Answer | [LeetCode 410](https://leetcode.com/problems/split-array-largest-sum/) |
| Find peak element | [LeetCode 162](https://leetcode.com/problems/find-peak-element/) |
| Search in Rotated Array | [LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| Find Rotation Count | GFG: Count Rotations |
| Smallest Missing Number | GFG: Missing Number in Sorted Array |
| Kth Element in Sorted Matrix | [LeetCode 378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |

---

## 🟠 Hard

| Problem | Platform |
|--------|----------|
| Allocate Minimum Pages | [GFG](https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1) |
| Aggressive Cows | [SPOJ AGGRCOW](https://www.spoj.com/problems/AGGRCOW/) |
| Painter's Partition Problem | [GFG](https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1) |
| Minimize Max Distance to Gas Station | [LeetCode 774](https://leetcode.com/problems/minimize-max-distance-to-gas-station/) |
| Capacity to Ship Packages in D Days | [LeetCode 1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |
| Minimize Largest Sum (Split Array) | [LeetCode 410](https://leetcode.com/problems/split-array-largest-sum/) |

---

## 🔴 Very Hard

| Problem | Platform |
|--------|----------|
| Median of Two Sorted Arrays | [LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) |
| Max Product Subarrays (with tricks) | Hybrid BS + 2 Pointer |
| Subarrays With Product Less Than K | [LeetCode 713](https://leetcode.com/problems/subarray-product-less-than-k/) |
| Infinite Sorted Array | GFG: Search in infinite array

---

## 🟣 God Tier

| Problem | Platform |
|--------|----------|
| Parametric Search with Functions | CF + AtCoder hard problems |
| Monotonic Function Search | CF + Hard LeetCode |
| Bitonic Array Search | GFG + Custom Practice |

---

## 🧠 CP-Level Binary Search

| Problem | Platform |
|--------|----------|
| Weighted Job Scheduling | [LeetCode 1235](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) |
| Coordinate Compression + BS | Codeforces 1660E |
| Binary Search + Segment Tree | CF Edu 2B, 2D |
| K-Median Optimization | AtCoder hard problems |

---

## 📘 Just Theory

| Topic | Note |
|-------|------|
| Binary Search Tree ≠ Binary Search | Tree traversal is not binary search |
| Ternary Search | Rarely used, but works on unimodal functions |
| Logarithmic Time Intuition | Interview explanation purpose only |

---

## 🗑️ Not Worth (Impractical)

| Situation | Why Not |
|-----------|---------|
| BS on Unsorted Arrays | Makes no sense |
| BS on Random Functions with No Monotonicity | Doesn't converge |
| Nested BS Without Constraints | Can be too slow |

---

## ✅ Tip to Remember:

> Use Binary Search when:
> - Input is **sorted** or **can be searched using monotonic logic**
> - You’re asked to **minimize/maximize something**
> - It feels like the answer lies between a **range** — try **Binary Search on answer**
