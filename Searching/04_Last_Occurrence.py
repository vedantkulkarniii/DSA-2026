"""
============================================================
  DSA-2026 | Searching | Problem 04
  Topic   : Last Occurrence in a Sorted Array
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array that may contain duplicate elements
    and a target value, find the index of the LAST (rightmost)
    occurrence of the target.
    Return -1 if the target is not present.

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate from RIGHT to LEFT and return the first index
    (from the right) where arr[index] == target.
    Or scan left-to-right, updating the result every time
    a match is found — the final stored value is the last.

------------------------------------------------------------
Optimized Approach — Modified Binary Search: O(log n)
------------------------------------------------------------
    Mirror image of the First Occurrence problem.

    Key Modification:
    - When arr[mid] == target, do NOT return immediately.
    - Record `mid` as a candidate answer and continue
      searching in the RIGHT half (left = mid + 1) to find
      a later (rightmost) occurrence.

    Steps:
    1. Initialize left=0, right=n-1, result=-1.
    2. While left <= right:
       a. Compute mid.
       b. If arr[mid] == target → save mid in result,
                                  search RIGHT half.
       c. If arr[mid] < target  → search RIGHT half.
       d. If arr[mid] > target  → search LEFT half.
    3. Return result.

    Comparison with First Occurrence:
        First Occurrence : on match, go LEFT  (right = mid - 1)
        Last Occurrence  : on match, go RIGHT (left  = mid + 1)

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity : O(log n) — single binary search pass.
    Space Complexity: O(1)     — no extra space used.

------------------------------------------------------------
Example:
    Input : arr = [1, 3, 5, 5, 5, 7, 9], target = 5
    Output: 4  (last occurrence of 5 is at index 4)

    Input : arr = [1, 3, 5, 5, 5, 7, 9], target = 6
    Output: -1
============================================================
"""


def last_occurrence(arr: list, target: int) -> int:
    """
    Find the last (rightmost) occurrence of target in a sorted array.

    Args:
        arr    (list): A sorted list of integers (may have duplicates).
        target (int) : The value to search for.

    Returns:
        int: Index of the last occurrence, or -1 if not found.
    """
    left = 0
    right = len(arr) - 1
    result = -1                         # Stores the best (rightmost) answer

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid                # Potential answer — keep looking right
            left = mid + 1             # Narrow search to the right half

        elif arr[mid] < target:
            left = mid + 1             # Target must be in the right half

        else:
            right = mid - 1            # Target must be in the left half

    return result


if __name__ == "__main__":
    print("=" * 55)
    print("  Last Occurrence — Test Cases")
    print("=" * 55)

    # Test Case 1: Multiple duplicates — last occurrence in middle
    arr1 = [1, 3, 5, 5, 5, 7, 9]
    print(f"\nArray  : {arr1}")
    print(f"Target : 5  → Index: {last_occurrence(arr1, 5)}")    # Expected: 4

    # Test Case 2: Target not present
    print(f"Target : 6  → Index: {last_occurrence(arr1, 6)}")    # Expected: -1

    # Test Case 3: Target appears only once
    print(f"Target : 7  → Index: {last_occurrence(arr1, 7)}")    # Expected: 5

    # Test Case 4: All elements are the same
    arr2 = [4, 4, 4, 4, 4]
    print(f"\nArray  : {arr2}")
    print(f"Target : 4  → Index: {last_occurrence(arr2, 4)}")    # Expected: 4

    # Test Case 5: Target duplicates at the end
    arr3 = [1, 2, 3, 5, 5]
    print(f"\nArray  : {arr3}")
    print(f"Target : 5  → Index: {last_occurrence(arr3, 5)}")    # Expected: 4

    # Test Case 6: Target duplicates at the beginning
    arr4 = [2, 2, 3, 4, 5]
    print(f"\nArray  : {arr4}")
    print(f"Target : 2  → Index: {last_occurrence(arr4, 2)}")    # Expected: 1

    # Test Case 7: Single element — found
    arr5 = [7]
    print(f"\nArray  : {arr5}")
    print(f"Target : 7  → Index: {last_occurrence(arr5, 7)}")    # Expected: 0

    # Test Case 8: Single element — not found
    print(f"Target : 3  → Index: {last_occurrence(arr5, 3)}")    # Expected: -1

    # Test Case 9: Empty array
    arr6 = []
    print(f"\nArray  : {arr6}")
    print(f"Target : 1  → Index: {last_occurrence(arr6, 1)}")    # Expected: -1

    print("\n" + "=" * 55)
