"""
============================================================
  DSA-2026 | Searching | Problem 08
  Topic   : Search Insert Position
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array of DISTINCT integers and a target,
    return the index if the target is found. If not found,
    return the index where it would be inserted to keep
    the array sorted.

    This is LeetCode Problem #35 — a very common interview question.

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate through the array:
    - If arr[i] == target, return i.
    - If arr[i] > target, return i (insert before this position).
    - If loop ends, return len(arr) (insert at the end).

------------------------------------------------------------
Optimized Approach — Binary Search: O(log n)
------------------------------------------------------------
    Key Insight:
    Search Insert Position is exactly the same as Lower Bound.
    - Lower Bound returns the first index where arr[i] >= target.
    - If target exists → lower bound = its index (exact match).
    - If target doesn't exist → lower bound = insertion point.

    Steps:
    1. Initialize left=0, right=n (covers the "insert at end" case).
    2. While left < right:
       a. Compute mid.
       b. If arr[mid] >= target → possible answer, go LEFT.
       c. If arr[mid] < target  → go RIGHT.
    3. Return left (= right at end of loop).

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity : O(log n) — single binary search pass.
    Space Complexity: O(1)     — no extra space.

------------------------------------------------------------
Connection to Lower Bound (Interview Insight):
------------------------------------------------------------
    search_insert_position(arr, target) == lower_bound(arr, target)

    Understanding this relationship demonstrates a deep
    understanding of Binary Search variants — impressive to interviewers.

------------------------------------------------------------
Example:
    Input : arr = [1, 3, 5, 6], target = 5
    Output: 2  (arr[2] = 5, target found)

    Input : arr = [1, 3, 5, 6], target = 2
    Output: 1  (insert between 1 and 3)

    Input : arr = [1, 3, 5, 6], target = 7
    Output: 4  (insert at the end)

    Input : arr = [1, 3, 5, 6], target = 0
    Output: 0  (insert at the beginning)
============================================================
"""


def search_insert_position(arr: list, target: int) -> int:
    """
    Return the index of target if found, or the index where
    it should be inserted to maintain sorted order.

    Args:
        arr    (list): A sorted list of distinct integers.
        target (int) : The value to search or insert.

    Returns:
        int: Index of target or its correct insertion position.
    """
    left = 0
    right = len(arr)            # right = n to handle "insert at end"

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            right = mid         # mid is a potential answer; search left

        else:
            left = mid + 1      # arr[mid] < target; discard left half

    # At the end of the loop, left == right == insertion position
    return left


def search_insert_brute(arr: list, target: int) -> int:
    """
    Search insert position using linear scan — O(n).

    Args:
        arr    (list): A sorted list of distinct integers.
        target (int) : The value to search or insert.

    Returns:
        int: Insertion index.
    """
    for i in range(len(arr)):
        if arr[i] >= target:
            return i
    return len(arr)


if __name__ == "__main__":
    print("=" * 55)
    print("  Search Insert Position — Test Cases")
    print("=" * 55)

    arr = [1, 3, 5, 6]
    print(f"\nArray: {arr}")

    # Test Case 1: Target found
    print(f"\nTarget : 5  → Insert Position: {search_insert_position(arr, 5)}")
    # Expected: 2

    # Test Case 2: Insert in the middle
    print(f"Target : 2  → Insert Position: {search_insert_position(arr, 2)}")
    # Expected: 1

    # Test Case 3: Insert at the end
    print(f"Target : 7  → Insert Position: {search_insert_position(arr, 7)}")
    # Expected: 4

    # Test Case 4: Insert at the beginning
    print(f"Target : 0  → Insert Position: {search_insert_position(arr, 0)}")
    # Expected: 0

    # Test Case 5: Target equals first element
    print(f"Target : 1  → Insert Position: {search_insert_position(arr, 1)}")
    # Expected: 0

    # Test Case 6: Target equals last element
    print(f"Target : 6  → Insert Position: {search_insert_position(arr, 6)}")
    # Expected: 3

    # Test Case 7: Single element — target found
    arr2 = [5]
    print(f"\nArray  : {arr2}")
    print(f"Target : 5  → Insert Position: {search_insert_position(arr2, 5)}")
    # Expected: 0

    # Test Case 8: Single element — insert before
    print(f"Target : 3  → Insert Position: {search_insert_position(arr2, 3)}")
    # Expected: 0

    # Test Case 9: Single element — insert after
    print(f"Target : 9  → Insert Position: {search_insert_position(arr2, 9)}")
    # Expected: 1

    # Test Case 10: Verify brute and optimized match
    arr3 = [2, 4, 6, 8, 10]
    print(f"\nArray: {arr3}")
    for t in [1, 3, 5, 7, 9, 11]:
        opt = search_insert_position(arr3, t)
        brute = search_insert_brute(arr3, t)
        match = "✓" if opt == brute else "✗"
        print(f"  Target: {t:2d} → Optimized: {opt}, Brute: {brute}  {match}")

    print("\n" + "=" * 55)
