# Searching — Concepts & Notes

> Author: Vedant Kulkarni | DSA-2026

---

## What is Searching?

Searching is the process of finding a specific element (called
the **target**) inside a data structure like an array or list.

Think of it like finding a book in a library. You have two options:
1. Check every shelf one by one (Linear Search).
2. Use the library's catalogue/index system (Binary Search).

---

## 1. Linear Search

### What is it?
Check every element one by one, from left to right, until you
find the target or reach the end.

### When to Use?
- Array is **unsorted**
- Array is very small
- You are searching in a Linked List (no random access)
- One-time search with no preprocessing

### Example
```
Array  : [4, 2, 7, 1, 9]
Target : 7

Step 1: Check index 0 → arr[0] = 4  ≠ 7
Step 2: Check index 1 → arr[1] = 2  ≠ 7
Step 3: Check index 2 → arr[2] = 7  = 7 → FOUND at index 2
```

### Complexity
| Case         | Time  | Space |
|--------------|-------|-------|
| Best Case    | O(1)  | O(1)  |
| Worst Case   | O(n)  | O(1)  |
| Average Case | O(n)  | O(1)  |

---

## 2. Binary Search

### What is it?
A smarter search that only works on a **sorted array**.
Instead of checking one element at a time, it checks the
**middle element** and eliminates half the array each step.

### The Key Idea (Divide and Conquer)
```
If middle == target  → Found!
If middle <  target  → Target must be in the RIGHT half
If middle >  target  → Target must be in the LEFT half
```

### Example
```
Array  : [1, 3, 5, 7, 9, 11, 13]
Target : 7

Step 1: left=0, right=6, mid=3 → arr[3] = 7 = target → FOUND
```

```
Array  : [1, 3, 5, 7, 9, 11, 13]
Target : 6

Step 1: left=0, right=6, mid=3 → arr[3] = 7 > 6 → go LEFT
Step 2: left=0, right=2, mid=1 → arr[1] = 3 < 6 → go RIGHT
Step 3: left=2, right=2, mid=2 → arr[2] = 5 < 6 → go RIGHT
Step 4: left=3 > right=2 → STOP → return -1 (not found)
```

### Why `mid = left + (right - left) // 2`?
This is the safe way to compute the middle index.
- `(left + right) // 2` can cause **integer overflow** in languages
  like Java/C++ for very large arrays.
- Python handles big integers natively, but it's good practice
  to always use the safe formula.

### Complexity
| Case         | Time     | Space (Iterative) | Space (Recursive) |
|--------------|----------|--------------------|-------------------|
| Best Case    | O(1)     | O(1)               | O(log n)          |
| Worst Case   | O(log n) | O(1)               | O(log n)          |
| Average Case | O(log n) | O(1)               | O(log n)          |

### Why O(log n)?
Each step cuts the search space in half.
- n=1,000      → at most 10 steps
- n=1,000,000  → at most 20 steps
- n=1,000,000,000 → at most 30 steps

That is the power of logarithmic time!

---

## 3. Linear Search vs Binary Search

| Feature           | Linear Search | Binary Search      |
|-------------------|---------------|--------------------|
| Array must be sorted? | No        | **Yes**            |
| Time Complexity   | O(n)          | O(log n)           |
| Space Complexity  | O(1)          | O(1) iterative     |
| Works on linked list? | Yes       | No (no random access) |
| Best for          | Small / unsorted arrays | Large sorted arrays |
| Preprocessing needed? | No        | Array must be sorted |

---

## 4. Binary Search Variants (All in this folder)

### First Occurrence
> Find the LEFTMOST index of target in a sorted array with duplicates.

**Trick:** When you find the target at `mid`, don't stop.
Save `mid` as the answer and search the **LEFT half** for an earlier occurrence.

```
On match → result = mid, go LEFT (right = mid - 1)
```

### Last Occurrence
> Find the RIGHTMOST index of target.

**Trick:** Mirror of First Occurrence.
When you find target at `mid`, save it and search the **RIGHT half**.

```
On match → result = mid, go RIGHT (left = mid + 1)
```

### Count Occurrences
> How many times does target appear?

**Formula:**
```
count = last_occurrence - first_occurrence + 1
```
Uses two binary searches → still O(log n).

### Lower Bound
> First index where `arr[i] >= target`

- Returns the **insertion point** for target.
- If target exists, returns its first index.
- If target doesn't exist, returns where it *would* go.

```
lower_bound([1,3,5,7], 5)  → 2 (arr[2] = 5)
lower_bound([1,3,5,7], 4)  → 2 (arr[2] = 5 >= 4, first such position)
```

### Upper Bound
> First index where `arr[i] > target`

```
upper_bound([1,3,5,7], 5)  → 3 (arr[3] = 7 is first > 5)
upper_bound([1,3,5,7], 4)  → 2 (arr[2] = 5 is first > 4)
```

**Key relationship:**
```
count of target = upper_bound(target) - lower_bound(target)
```

### Search Insert Position
> Where should target go to keep the array sorted?

This is EXACTLY the same as Lower Bound.
- If target exists → return its index.
- If target doesn't exist → return where it should be inserted.

### Floor of Number
> Greatest element in the array that is <= target.

```
Array: [1, 2, 4, 6, 10]
Floor of 7  = 6   (largest element <= 7)
Floor of 0  = -1  (no element <= 0)
Floor of 10 = 10  (exact match)
```

**Trick:** When `arr[mid] < target`, save it as a candidate
and go **RIGHT** (maybe a larger valid value exists).

### Ceil of Number
> Smallest element in the array that is >= target.

```
Array: [1, 2, 4, 6, 10]
Ceil of 3   = 4   (smallest element >= 3)
Ceil of 11  = -1  (no element >= 11)
Ceil of 6   = 6   (exact match)
```

**Trick:** When `arr[mid] > target`, save it as a candidate
and go **LEFT** (maybe a smaller valid value exists).

---

## 5. Binary Search Cheat Sheet

```
Standard Binary Search
    On match  → return mid
    arr[mid] < target → left  = mid + 1
    arr[mid] > target → right = mid - 1

First Occurrence
    On match  → result = mid, right = mid - 1  (go LEFT)

Last Occurrence
    On match  → result = mid, left  = mid + 1  (go RIGHT)

Lower Bound  (first index where arr[i] >= target)
    arr[mid] >= target → result = mid, right = mid    (go LEFT)
    arr[mid] <  target → left = mid + 1               (go RIGHT)

Upper Bound  (first index where arr[i] > target)
    arr[mid] >  target → result = mid, right = mid    (go LEFT)
    arr[mid] <= target → left = mid + 1               (go RIGHT)

Floor  (greatest element <= target)
    arr[mid] == target → return arr[mid]
    arr[mid] <  target → floor = arr[mid], left = mid + 1   (go RIGHT)
    arr[mid] >  target → right = mid - 1                    (go LEFT)

Ceil   (smallest element >= target)
    arr[mid] == target → return arr[mid]
    arr[mid] >  target → ceil = arr[mid], right = mid - 1   (go LEFT)
    arr[mid] <  target → left = mid + 1                     (go RIGHT)
```

---

## 6. Prerequisite for Binary Search

Binary Search can ONLY be applied when:
1. The array (or search space) is **sorted** (or monotonic).
2. You can access elements by index in O(1) — **random access**.
3. You can define a clear **condition** that splits the space
   into two halves: one where the answer lies, one where it doesn't.

---

## 7. Common Mistakes to Avoid

| Mistake | Correct Approach |
|---------|-----------------|
| `mid = (left + right) // 2` | Use `mid = left + (right - left) // 2` |
| `while left < right` for standard BS | Use `while left <= right` |
| `right = n - 1` for Lower/Upper Bound | Use `right = n` |
| Returning on first match for First Occurrence | Save result, keep searching left |
| Modifying input array before sorting | Always search on the original sorted array |

---

## 8. Complexity Summary Table

| Algorithm              | Time       | Space  |
|------------------------|------------|--------|
| Linear Search          | O(n)       | O(1)   |
| Binary Search          | O(log n)   | O(1)   |
| First Occurrence       | O(log n)   | O(1)   |
| Last Occurrence        | O(log n)   | O(1)   |
| Count Occurrences      | O(log n)   | O(1)   |
| Lower Bound            | O(log n)   | O(1)   |
| Upper Bound            | O(log n)   | O(1)   |
| Search Insert Position | O(log n)   | O(1)   |
| Floor of Number        | O(log n)   | O(1)   |
| Ceil of Number         | O(log n)   | O(1)   |

---

*These notes are part of the DSA-2026 repository by Vedant Kulkarni.*
*Keep practicing. Consistency beats intensity.*
