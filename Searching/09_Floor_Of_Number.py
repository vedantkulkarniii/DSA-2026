"""
============================================================
  DSA-2026 | Searching | Problem 09
  Topic   : Floor of a Number in a Sorted Array
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array and a target value, find the FLOOR
    of the target — the greatest element in the array that
    is less than or equal to the target (element <= target).

    Return the floor value. If no such element exists
    (all elements > target), return -1.

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate through the sorted array and track the last
    element that is <= target. Return it at the end.

------------------------------------------------------------
Optimized Approach — Binary Search: O(log n)
------------------------------------------------------------
    Key Insight:
    In a sorted array, all elements <= target are in the
    left portion. We want the rightmost one among them.

    Modified Binary Search:
    1. Initialize left=0, right=n-1, floor=-1 (not found).
    2. While left <= right:
       a. Compute mid.
       b. If arr[mid] == target → exact match, return arr[mid].
       c. If arr[mid] < target  → arr[mid] is a valid floor candidate.
                                  Save arr[mid] in floor.
                                  Go RIGHT to find a better (larger) candidate.
       d. If arr[mid] > target  → arr[mid] is too large.
                                  Go LEFT.
    3. Return floor.

    Why go RIGHT when arr[mid] < target?
    Because we want the GREATEST value <= target.
    Going right might find a value closer to target.

------------------------------------------------------------
Floor vs Lower Bound (Interview Insight):
------------------------------------------------------------
    Lower Bound : returns INDEX of first element >= target
    Floor       : returns VALUE of greatest element <= target

    They search in opposite directions for opposite conditions.

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity : O(log n) — single binary search pass.
    Space Complexity: O(1)     — no extra space used.

------------------------------------------------------------
Example:
    Input : arr = [1, 2, 4, 6, 10, 12, 14], target = 7
    Output: 6  (greatest element <= 7 is 6)

    Input : arr = [1, 2, 4, 6, 10, 12, 14], target = 10
    Output: 10 (exact match)

    Input : arr = [1, 2, 4, 6, 10, 12, 14], target = 0
    Output: -1 (no element <= 0)
============================================================
"""


def floor_of_number(arr: list, target: int) -> int:
    """
    Find the floor of target in a sorted array.

    Floor = greatest element in arr that is <= target.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The reference value.

    Returns:
        int: The floor value, or -1 if no floor exists.
    """
    if not arr or arr[0] > target:
        return -1               # All elements are greater than target

    left = 0
    right = len(arr) - 1
    floor = -1                  # Stores the best floor found so far

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid]     # Exact match — this IS the floor

        elif arr[mid] < target:
            floor = arr[mid]    # Valid floor candidate — save it
            left = mid + 1      # Go right to find a closer (larger) value

        else:
            right = mid - 1     # arr[mid] > target — go left

    return floor


if __name__ == "__main__":
    print("=" * 55)
    print("  Floor of Number — Test Cases")
    print("=" * 55)

    arr = [1, 2, 4, 6, 10, 12, 14]
    print(f"\nArray: {arr}")

    # Test Case 1: Target between two elements
    print(f"\nTarget : 7  → Floor: {floor_of_number(arr, 7)}")    # Expected: 6

    # Test Case 2: Exact match
    print(f"Target : 10 → Floor: {floor_of_number(arr, 10)}")     # Expected: 10

    # Test Case 3: Target smaller than all elements
    print(f"Target : 0  → Floor: {floor_of_number(arr, 0)}")      # Expected: -1

    # Test Case 4: Target larger than all elements
    print(f"Target : 15 → Floor: {floor_of_number(arr, 15)}")     # Expected: 14

    # Test Case 5: Target equals the first element
    print(f"Target : 1  → Floor: {floor_of_number(arr, 1)}")      # Expected: 1

    # Test Case 6: Target equals the last element
    print(f"Target : 14 → Floor: {floor_of_number(arr, 14)}")     # Expected: 14

    # Test Case 7: Array with duplicates
    arr2 = [1, 2, 2, 4, 4, 6]
    print(f"\nArray  : {arr2}")
    print(f"Target : 3  → Floor: {floor_of_number(arr2, 3)}")     # Expected: 2
    print(f"Target : 4  → Floor: {floor_of_number(arr2, 4)}")     # Expected: 4
    print(f"Target : 5  → Floor: {floor_of_number(arr2, 5)}")     # Expected: 4

    # Test Case 8: Single element
    arr3 = [5]
    print(f"\nArray  : {arr3}")
    print(f"Target : 5  → Floor: {floor_of_number(arr3, 5)}")     # Expected: 5
    print(f"Target : 3  → Floor: {floor_of_number(arr3, 3)}")     # Expected: -1
    print(f"Target : 9  → Floor: {floor_of_number(arr3, 9)}")     # Expected: 5

    # Test Case 9: Empty array
    arr4 = []
    print(f"\nArray  : {arr4}")
    print(f"Target : 5  → Floor: {floor_of_number(arr4, 5)}")     # Expected: -1

    print("\n" + "=" * 55)
