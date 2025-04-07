<details>
<summary>Sliding Window Basics</summary>

  ## SlidingWindow

- Sliding window in short take a space let's just say 3 blocks and move it in a linear way
- So when moving from left to right or vice versa try adding the new block while removing the block we are exiting
- ![image](https://github.com/user-attachments/assets/df934a06-a568-4f51-8d61-4660fc33b5c2)
- What insights could we be getting here
  1. While removing a value and adding a new value we are getting a update value of a subarray of size k which can be maximum or not
  2. if it then we are getting the maximun value of the subarray or not
- All the possible kind of Questions that fall into the sliding window concept are below
  1.Maximum/Minimum Subarray Sum:
  2.Longest Substring with K Distinct Characters:
  3.Longest Subarray with Ones after Replacement:
  4.Find All Anagrams in a String:
  5.Smallest Subarray with Sum at Least K:
  6.Maximum Consecutive Ones after Flipping Zeros:
  7.Minimum Window Substring:
  8.Longest Repeating Character Replacement:
  9.Fruit Into Baskets:
  10.Subarrays with Product Less than K:

  > Definition:
  **Sliding window algorithm is a problem solving technique that transforms two nested loops into one loop. It can reduce the time complexity of an algorithm to O(n).**

## What Is the Sliding Window Algorithm?
### some fundamental clues to identify sliding window algorithm problems:

1.*Sequential Linear Data Structures :* The problem will be based on an array, list or string type of data structure.

2.It will ask to find **subranges** in that array to give the *longest, shortest or target values of a string*.

3.Its concept is mainly based on ideas like the **longest sequence or shortest sequence** of something that satisfies a given condition perfectly.

### Visual Representation

![image](https://github.com/user-attachments/assets/edfa763d-3754-4368-b7b9-eebf3fd5c501)

**How Sliding Works Bruh**

![image](https://github.com/user-attachments/assets/e683666c-c95b-4bc8-baba-f6a0bd074e5d)

> ⚠️ **Important:** I believe the sliding window algorithm is more of a technique than an algorithm since it's a key ingrident in many other algorithms.
> https://builtin.com/data-science/sliding-window-algorithm#:~:text=The%20sliding%20window%20technique%20moves,end%20of%20the%20data%20structure.

</details>
