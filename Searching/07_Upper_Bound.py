"""
============================================================
  DSA-2026 | Searching | Problem 07
  Topic   : Upper Bound
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array and a target value, find the
    UPPER BOUND — the index of the first element that is
    strictly greater than the target (element > target).

    If no such element exists (all elements <= target),
    return len(arr) (one past the last index).

    This mirrors C++ STL's std::upper_bound().

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate left to right and return the first index where
    arr[i] > target.

------------------------------------------------------------
Optimized Approach — Binary Search: O(log n)
------------------------------------------------------------
    Very similar to Lower Bound with one key difference:
    - Lower Bound : arr[mid] >= target → valid candidate
    - Upper Bound : arr[mid] >  target → valid candidate

    Steps:
    1. Initialize left=0, right=n, result=n.
    2. While left < right:
       a. Compute mid.
       b. If arr[mid] > target  → mid is valid candidate.
                                  Save mid, search LEFT.
       c. If arr[mid] <= target → search RIGHT (left = mid+1).
    3. Return result.

------------------------------------------------------------
Lower Bound vs Upper Bound (Key Comparison):
------------------------------------------------------------
    Lower Bound : first index where arr[i] >= target
    Upper Bound : first index where arr[i] >  target

    Together they define the range [lower, upper) in which
    all occurrences of target lie.

    Count of target = upper_bound(target) - lower_bound(target)

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity : O(log n) — single binary search pass.
    Space Complexity: O(1)     — no extra space used.

------------------------------------------------------------
Example:
    Input : arr = [1, 3, 5, 7, 9, 11], target = 7
    Output: 4  (arr[4] = 9 is first element > 7)

    Input : arr = [1, 3, 5, 7, 9, 11], target = 6
    Output: 3  (arr[3] = 7 is first element > 6)

    Input : arr = [1, 3, 5, 7, 9, 11], target = 11
    Output: 6  (no element > 11, return len(arr))
============================================================
"""


def upper_bound(arr: list, target: int) -> int:
    """
    Find the upper bound — first index where arr[i] > target.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The reference value.

    Returns:
        int: First index i such that arr[i] > target.
             Returns len(arr) if all elements are <= target.
    """
    left = 0
    right = len(arr)            # Note: right = n, not n-1
    result = len(arr)           # Default: no valid position found

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > target:
            result = mid        # Valid candidate — try to find earlier
            right = mid         # Search left half

        else:
            left = mid + 1      # arr[mid] <= target — go right

    return result


def count_using_bounds(arr: list, target: int) -> int:
    """
    Count occurrences of target using upper_bound - lower_bound.

    Demonstrates the relationship between Lower and Upper Bound.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The value to count.

    Returns:
        int: Number of times target appears in arr.
    """
    from bisect import bisect_left, bisect_right
    # bisect_left  = lower_bound
    # bisect_right = upper_bound
    return bisect_right(arr, target) - bisect_left(arr, target)


if __name__ == "__main__":
    print("=" * 55)
    print("  Upper Bound — Test Cases")
    print("=" * 55)

    arr = [1, 3, 5, 7, 9, 11]
    print(f"\nArray: {arr}")

    # Test Case 1: Target exists — return index after last occurrence
    idx1 = upper_bound(arr, 7)
    print(f"\nTarget : 7  → Upper Bound Index: {idx1}")
    print(f"           → arr[{idx1}] = {arr[idx1]}")
    # Expected: 4 (arr[4] = 9 is first > 7)

    # Test Case 2: Target between elements
    idx2 = upper_bound(arr, 6)
    print(f"\nTarget : 6  → Upper Bound Index: {idx2}")
    print(f"           → arr[{idx2}] = {arr[idx2]}")
    # Expected: 3 (arr[3] = 7 is first > 6)

    # Test Case 3: Target less than all
    idx3 = upper_bound(arr, 0)
    print(f"\nTarget : 0  → Upper Bound Index: {idx3}")
    print(f"           → arr[{idx3}] = {arr[idx3]}")
    # Expected: 0

    # Test Case 4: Target greater than all
    idx4 = upper_bound(arr, 11)
    print(f"\nTarget : 11 → Upper Bound Index: {idx4}")
    print(f"           → Equals len(arr)={len(arr)}: {idx4 == len(arr)}")
    # Expected: 6

    # Test Case 5: Array with duplicates — count via bounds
    arr2 = [1, 2, 2, 2, 3, 4]
    print(f"\nArray  : {arr2}")
    lb = 1  # lower_bound of 2 = 1
    ub = upper_bound(arr2, 2)
    print(f"Target : 2  → Upper Bound: {ub}")
    print(f"Count of 2  = upper_bound - lower_bound = {ub} - {lb} = {ub - lb}")
    # Expected: Upper Bound = 4, Count = 3

    # Test Case 6: Single element
    arr3 = [5]
    print(f"\nArray  : {arr3}")
    print(f"Target : 5  → Upper Bound: {upper_bound(arr3, 5)}")  # 1 (=len)
    print(f"Target : 4  → Upper Bound: {upper_bound(arr3, 4)}")  # 0
    print(f"Target : 6  → Upper Bound: {upper_bound(arr3, 6)}")  # 1

    print("\n" + "=" * 55)
