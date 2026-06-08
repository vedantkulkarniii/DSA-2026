"""
============================================================
  DSA-2026 | Searching | Problem 06
  Topic   : Lower Bound
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array and a target value, find the
    LOWER BOUND — the index of the first element that is
    greater than or equal to the target (element >= target).

    If no such element exists (all elements < target),
    return len(arr) (one past the last index).

    This mirrors C++ STL's std::lower_bound().

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate left to right and return the first index where
    arr[i] >= target.

------------------------------------------------------------
Optimized Approach — Binary Search: O(log n)
------------------------------------------------------------
    Key Insight:
    - We are NOT searching for an exact match.
    - We want the leftmost position where arr[i] >= target.

    Modified Binary Search:
    1. Initialize left=0, right=n (not n-1!), result=n.
    2. While left < right (note: strict less-than):
       a. Compute mid.
       b. If arr[mid] >= target → mid is a valid candidate.
                                  Save mid in result.
                                  Search LEFT (right = mid).
       c. If arr[mid] < target  → Search RIGHT (left = mid+1).
    3. Return result.

    Why right = n?
    - The answer could be n if all elements are < target.
    - Setting right = n ensures we cover that case.

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity : O(log n) — single binary search pass.
    Space Complexity: O(1)     — no extra space used.

------------------------------------------------------------
Real-World Use Cases (Interview Tip):
------------------------------------------------------------
    - Scheduling: find the earliest available time slot.
    - Database range queries.
    - Foundation for Count Occurrences (First Occurrence = Lower Bound).

------------------------------------------------------------
Example:
    Input : arr = [1, 3, 5, 7, 9, 11], target = 6
    Output: 3  (arr[3] = 7 is the first element >= 6)

    Input : arr = [1, 3, 5, 7, 9, 11], target = 7
    Output: 3  (arr[3] = 7 is the first element >= 7)

    Input : arr = [1, 3, 5, 7, 9, 11], target = 12
    Output: 6  (no element >= 12, return len(arr))
============================================================
"""


def lower_bound(arr: list, target: int) -> int:
    """
    Find the lower bound — first index where arr[i] >= target.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The reference value.

    Returns:
        int: First index i such that arr[i] >= target.
             Returns len(arr) if all elements are < target.
    """
    left = 0
    right = len(arr)            # Note: right = n, not n-1
    result = len(arr)           # Default: no valid position found

    while left < right:         # Note: strict less-than
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            result = mid        # Valid candidate — try to find earlier
            right = mid         # Search left half (right = mid, not mid-1)

        else:
            left = mid + 1      # arr[mid] < target — go right

    return result


if __name__ == "__main__":
    print("=" * 55)
    print("  Lower Bound — Test Cases")
    print("=" * 55)

    arr = [1, 3, 5, 7, 9, 11]
    print(f"\nArray: {arr}")

    # Test Case 1: Target exists in array
    print(f"\nTarget : 7  → Lower Bound Index: {lower_bound(arr, 7)}")
    print(f"           → arr[{lower_bound(arr, 7)}] = {arr[lower_bound(arr, 7)]}")
    # Expected: 3 (arr[3] = 7)

    # Test Case 2: Target between two elements
    print(f"\nTarget : 6  → Lower Bound Index: {lower_bound(arr, 6)}")
    print(f"           → arr[{lower_bound(arr, 6)}] = {arr[lower_bound(arr, 6)]}")
    # Expected: 3 (arr[3] = 7 is first >= 6)

    # Test Case 3: Target less than all elements
    print(f"\nTarget : 0  → Lower Bound Index: {lower_bound(arr, 0)}")
    print(f"           → arr[{lower_bound(arr, 0)}] = {arr[lower_bound(arr, 0)]}")
    # Expected: 0 (arr[0] = 1 is first >= 0)

    # Test Case 4: Target greater than all elements
    idx4 = lower_bound(arr, 12)
    print(f"\nTarget : 12 → Lower Bound Index: {idx4}")
    print(f"           → Index equals len(arr) = {len(arr)}: {idx4 == len(arr)}")
    # Expected: 6 (no element >= 12)

    # Test Case 5: Target equals smallest element
    print(f"\nTarget : 1  → Lower Bound Index: {lower_bound(arr, 1)}")
    # Expected: 0

    # Test Case 6: Array with duplicates
    arr2 = [1, 2, 2, 2, 3, 4]
    print(f"\nArray  : {arr2}")
    print(f"Target : 2  → Lower Bound Index: {lower_bound(arr2, 2)}")
    # Expected: 1 (first occurrence of 2)

    # Test Case 7: Single element
    arr3 = [5]
    print(f"\nArray  : {arr3}")
    print(f"Target : 5  → Lower Bound Index: {lower_bound(arr3, 5)}")  # 0
    print(f"Target : 6  → Lower Bound Index: {lower_bound(arr3, 6)}")  # 1 (=len)
    print(f"Target : 4  → Lower Bound Index: {lower_bound(arr3, 4)}")  # 0

    print("\n" + "=" * 55)
