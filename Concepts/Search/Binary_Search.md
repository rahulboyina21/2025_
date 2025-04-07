# Binary Search
<details>
<summary><strong><italic>This is the Plan</italic></strong></summary>
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
</details>
<details>
   <summary><strong>Forms and Shapes</strong></summary>
   #💀 Binary Search in Disguise – The Many Forms of BS

Binary Search isn't just a "find the number" technique — it's a shape-shifter that keeps changing outfits across problems. Here's a list of how BS shows up in twisted ways and how to think about each.

---

| 🎭 Version                | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **Classic BS**           | Find exact number in a sorted array. Basic and clean. ✅                    |
| **First Occurrence**     | After finding the match, keep moving **left** to get the first position.   |
| **Last Occurrence**      | After finding the match, keep moving **right** to get the last position.   |
| **Insert Position**      | If target not found, return the index where it should be inserted.         |
| **Rotated Sorted Array** | Find element in a rotated array — mid logic depends on sorted halves. 😵    |
| **Peak Element**         | Use slope (`nums[mid] < nums[mid+1]`) to climb to a peak. 🧗                |
| **Mountain Array**       | First binary search to find peak, then search left/right for target.       |
| **Min in Rotated Array** | Compare `nums[mid]` with `nums[end]` to decide direction.                  |
| **Search in 2D Matrix**  | Treat matrix as 1D or do row-col wise BS.                                  |
| **Search in Infinite Array** | Expand range exponentially, then apply BS.                           |
| **Find K-th Element**    | Combine BS with logic to count elements <= mid from multiple arrays.       |
| **Count of Target**      | Find first and last occurrence → count = last - first + 1.                 |

---

## 🧠 How to Think About Any BS Problem

1. Can I divide the array into two halves meaningfully?
2. What condition lets me throw away one half?
3. Do I return immediately or explore further?

---

> **BS ain't just a function — it's a damn martial art. 🥋**  
> Learn the forms. Spot the pattern. Control the chaos.


### Addon's 01 


Here you go, bruh — the **God-Tier Binary Search Guide** in pure Markdown format, ready to copy and paste:

---

```md
# 🧠 Binary Search – God Tier Mastery Guide

Welcome to the **final form** of Binary Search mastery. This document takes you from standard patterns to deep, rarely-discussed tricks used in high-level CP, Leetcode hards, and interviews.

---

## 🔁 Core Binary Search Template

```python
low, high = 0, len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if condition(mid):
        high = mid - 1
    else:
        low = mid + 1
```

---

## 🧰 Must-Know Patterns & Variants

| 🎭 Pattern                   | What It Does                                                        |
|-----------------------------|----------------------------------------------------------------------|
| **Classic Search**          | Search for exact element in sorted array                            |
| **Lower Bound**             | First index `>= target` (insert position)                           |
| **Upper Bound**             | First index `> target`                                              |
| **First/Last Occurrence**   | Modify condition to store mid & keep searching                      |
| **Binary Search on Answer** | Search in value range not array indices                             |
| **Search in Rotated Array** | Split logic based on sorted half                                    |
| **Find Peak**               | Use slope logic (`nums[mid] < nums[mid+1]`)                         |
| **Mountain Array**          | First find peak, then search left/right                             |
| **Aggressive Cows (GFG)**   | Maximize the minimum distance using binary search on answer         |
| **Koko Eating Bananas**     | Minimize speed where condition holds                                |
| **Minimum in Rotated Array**| Use comparison with `nums[end]`                                     |
| **Median of Two Arrays**    | Partition-based binary search on indexes                            |
| **Infinite Array Search**   | Expand right exponentially, then binary search                      |
| **BS in Matrix**            | Treat 2D matrix as 1D or use row + col individually                 |
| **Minimize Max (Split Array)**| Use binary search on sum bounds                                  |
| **Predicate Problems**      | Use BS to find first `True` in a `False -> True` sequence           |
| **Capacity Check Problems** | Use BS to find smallest capacity that works                         |

---

## 💡 Bonus Concepts

### 🧭 Binary Search on Functions

If a function `f(x)` is monotonic (non-increasing or non-decreasing), you can binary search on `x` to find thresholds like:
- Smallest `x` such that `f(x) >= K`
- Largest `x` such that `f(x) <= K`

---

### 🔄 BS Without Indices

Use this for problems like:
- Min days to ship packages
- Max size of smallest group
- Smallest divisor given threshold

Start with:
```python
low = 1
high = max(possible values)
```

---

## 📚 Must-Practice Problems

- Leetcode 33: Search in Rotated Sorted Array
- Leetcode 34: Find First and Last Position
- Leetcode 69: Sqrt(x)
- Leetcode 153: Min in Rotated Array
- Leetcode 162: Find Peak Element
- Leetcode 378: Kth Smallest in Matrix
- Leetcode 410: Split Array Largest Sum
- Leetcode 875: Koko Eating Bananas
- Leetcode 1011: Capacity to Ship Packages
- Leetcode 1283: Smallest Divisor

---

## 🧙 Mental Models

- “Can I make a binary decision at mid?”
- “What happens if I discard left or right half?”
- “Am I guaranteed to find an answer or should I store mid?”
- “Is my array value sorted or my condition?”

---

## ✅ Checkpoints for Bug-Free BS

- Prevent overflow: `mid = low + (high - low) // 2`
- Don't miss edge cases: `len == 1`, `mid+1`, `mid-1`
- Know whether to return `low`, `high`, or saved `ans`
- Avoid infinite loop: use `low <= high` or `low < high` with care
- Use helper `condition()` for readability

---

## 🔗 Top Resources

- [Leetcode Explore: Binary Search](https://leetcode.com/explore/learn/card/binary-search/)
- [CP Algorithms – Binary Search](https://cp-algorithms.com/)
- [Errichto's BS Patterns](https://www.youtube.com/watch?v=GU7DpgHINWQ)
- [Huahua's Leetcode Templates](https://github.com/wisdompeak/LeetCode/blob/master/Templates/Binary_Search.md)
- [Neetcode.io BS Patterns](https://neetcode.io/roadmap)

---

> **Binary Search isn't just a technique. It's a thinking tool.**  
> Master it once, and you'll cut through the hardest problems like butter 🔪🧈
```

---

Let me know if you want a version with visuals or a flowchart too, my bruh 💪
</details>
