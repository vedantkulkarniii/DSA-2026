"""
============================================================
  DSA-2026 | Searching | Problem 10
  Topic   : Ceil of a Number in a Sorted Array
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array and a target value, find the CEIL
    of the target — the smallest element in the array that
    is greater than or equal to the target (element >= target).

    Return the ceil value. If no such element exists
    (all elements < target), return -1.

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate through the sorted array left to right and return
    the first element that is >= target.

------------------------------------------------------------
Optimized Approach — Binary Search: O(log n)
------------------------------------------------------------
    Key Insight:
    Ceil is the mirror of Floor. We want the SMALLEST value
    that is >= target — the leftmost valid candidate.

    Modified Binary Search:
    1. Initialize left=0, right=n-1, ceil=-1.
    2. While left <= right:
       a. Compute mid.
       b. If arr[mid] == target → exact match, return arr[mid].
       c. If arr[mid] > target  → arr[mid] is a valid ceil candidate.
                                  Save arr[mid] in ceil.
                                  Go LEFT to find a smaller valid value.
       d. If arr[mid] < target  → arr[mid] too small, go RIGHT.
    3. Return ceil.

    Why go LEFT when arr[mid] > target?
    Because we want the SMALLEST value >= target.
    Going left might find a value closer to target.

------------------------------------------------------------
Ceil vs Lower Bound (Important Connection):
------------------------------------------------------------
    lower_bound(arr, target) gives the INDEX of the ceil.
    ceil_of_number(arr, target) gives the VALUE at that index.

    Ceil value = arr[lower_bound(arr, target)]
               (if lower_bound != len(arr))

------------------------------------------------------------
Floor vs Ceil Summary:
------------------------------------------------------------
    Floor : greatest element  <= target  (go RIGHT on miss)
    Ceil  : smallest element  >= target  (go LEFT  on miss)

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity : O(log n) — single binary search pass.
    Space Complexity: O(1)     — no extra space used.

------------------------------------------------------------
Example:
    Input : arr = [1, 2, 4, 6, 10, 12, 14], target = 7
    Output: 10 (smallest element >= 7 is 10)

    Input : arr = [1, 2, 4, 6, 10, 12, 14], target = 6
    Output: 6  (exact match)

    Input : arr = [1, 2, 4, 6, 10, 12, 14], target = 15
    Output: -1 (no element >= 15)
============================================================
"""


def ceil_of_number(arr: list, target: int) -> int:
    """
    Find the ceil of target in a sorted array.

    Ceil = smallest element in arr that is >= target.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The reference value.

    Returns:
        int: The ceil value, or -1 if no ceil exists.
    """
    if not arr or arr[-1] < target:
        return -1               # All elements are smaller than target

    left = 0
    right = len(arr) - 1
    ceil = -1                   # Stores the best ceil found so far

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid]     # Exact match — this IS the ceil

        elif arr[mid] > target:
            ceil = arr[mid]     # Valid ceil candidate — save it
            right = mid - 1     # Go left to find a smaller valid value

        else:
            left = mid + 1      # arr[mid] < target — go right

    return ceil


if __name__ == "__main__":
    print("=" * 55)
    print("  Ceil of Number — Test Cases")
    print("=" * 55)

    arr = [1, 2, 4, 6, 10, 12, 14]
    print(f"\nArray: {arr}")

    # Test Case 1: Target between two elements
    print(f"\nTarget : 7  → Ceil: {ceil_of_number(arr, 7)}")     # Expected: 10

    # Test Case 2: Exact match
    print(f"Target : 6  → Ceil: {ceil_of_number(arr, 6)}")      # Expected: 6

    # Test Case 3: Target smaller than all elements
    print(f"Target : 0  → Ceil: {ceil_of_number(arr, 0)}")      # Expected: 1

    # Test Case 4: Target larger than all elements
    print(f"Target : 15 → Ceil: {ceil_of_number(arr, 15)}")     # Expected: -1

    # Test Case 5: Target equals the first element
    print(f"Target : 1  → Ceil: {ceil_of_number(arr, 1)}")      # Expected: 1

    # Test Case 6: Target equals the last element
    print(f"Target : 14 → Ceil: {ceil_of_number(arr, 14)}")     # Expected: 14

    # Test Case 7: Array with duplicates
    arr2 = [1, 2, 2, 4, 4, 6]
    print(f"\nArray  : {arr2}")
    print(f"Target : 3  → Ceil: {ceil_of_number(arr2, 3)}")     # Expected: 4
    print(f"Target : 4  → Ceil: {ceil_of_number(arr2, 4)}")     # Expected: 4
    print(f"Target : 5  → Ceil: {ceil_of_number(arr2, 5)}")     # Expected: 6

    # Test Case 8: Single element
    arr3 = [5]
    print(f"\nArray  : {arr3}")
    print(f"Target : 5  → Ceil: {ceil_of_number(arr3, 5)}")     # Expected: 5
    print(f"Target : 3  → Ceil: {ceil_of_number(arr3, 3)}")     # Expected: 5
    print(f"Target : 9  → Ceil: {ceil_of_number(arr3, 9)}")     # Expected: -1

    # Test Case 9: Empty array
    arr4 = []
    print(f"\nArray  : {arr4}")
    print(f"Target : 5  → Ceil: {ceil_of_number(arr4, 5)}")     # Expected: -1

    # Test Case 10: Floor and Ceil together (complete picture)
    # Floor helper defined inline so this file stays self-contained
    def _floor(a, tgt):
        if not a or a[0] > tgt:
            return -1
        lo, hi, fl = 0, len(a) - 1, -1
        while lo <= hi:
            md = lo + (hi - lo) // 2
            if a[md] == tgt:
                return a[md]
            elif a[md] < tgt:
                fl = a[md]
                lo = md + 1
            else:
                hi = md - 1
        return fl

    arr5 = [2, 3, 5, 9, 14, 16, 18]
    print(f"\nArray  : {arr5}")
    print(f"{'Target':>8} | {'Floor':>8} | {'Ceil':>8}")
    print("-" * 30)
    for t in [1, 3, 6, 9, 15, 20]:
        f = _floor(arr5, t)
        c = ceil_of_number(arr5, t)
        print(f"{t:>8} | {f:>8} | {c:>8}")

    print("\n" + "=" * 55)
