"""
============================================================
  DSA-2026 | Searching | Problem 05
  Topic   : Count Occurrences in a Sorted Array
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a sorted array and a target value, count how many
    times the target appears in the array.

------------------------------------------------------------
Brute Force — Linear Scan: O(n)
------------------------------------------------------------
    Iterate through the array and increment a counter every
    time arr[i] == target.
    Simple but doesn't exploit sorted order.

------------------------------------------------------------
Optimized Approach — Two Binary Searches: O(log n)
------------------------------------------------------------
    Key Insight:
    In a sorted array, all occurrences of a value are
    grouped together in a contiguous block.

    Strategy:
    1. Find the FIRST occurrence index using modified
       Binary Search (search left on match).
    2. Find the LAST occurrence index using modified
       Binary Search (search right on match).
    3. If target is not found (first == -1), return 0.
    4. Count = last_index - first_index + 1.

    This reduces O(n) to O(log n) — a significant
    improvement for large arrays.

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Brute Force:
        Time : O(n)     Space: O(1)

    Optimized:
        Time : O(log n) — two binary searches.
        Space: O(1)     — no extra space used.

------------------------------------------------------------
Example:
    Input : arr = [1, 2, 2, 2, 3, 4, 5], target = 2
    Output: 3

    Input : arr = [1, 2, 2, 2, 3, 4, 5], target = 6
    Output: 0
============================================================
"""


def first_occurrence(arr: list, target: int) -> int:
    """Find the first (leftmost) index of target. Returns -1 if absent."""
    left, right, result = 0, len(arr) - 1, -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1        # Go left to find earlier occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_occurrence(arr: list, target: int) -> int:
    """Find the last (rightmost) index of target. Returns -1 if absent."""
    left, right, result = 0, len(arr) - 1, -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1         # Go right to find later occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def count_occurrences(arr: list, target: int) -> int:
    """
    Count the total number of times target appears in a sorted array.

    Uses two binary searches to find first and last occurrences,
    then computes count = last - first + 1.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The value to count.

    Returns:
        int: Number of times target appears. 0 if not found.
    """
    first = first_occurrence(arr, target)

    # If target doesn't exist at all, skip the second search
    if first == -1:
        return 0

    last = last_occurrence(arr, target)

    return last - first + 1


def count_occurrences_brute(arr: list, target: int) -> int:
    """
    Count occurrences using linear scan — O(n) brute force.

    Args:
        arr    (list): A list of integers.
        target (int) : The value to count.

    Returns:
        int: Number of times target appears.
    """
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count


if __name__ == "__main__":
    print("=" * 55)
    print("  Count Occurrences — Test Cases")
    print("=" * 55)

    # Test Case 1: Multiple occurrences
    arr1 = [1, 2, 2, 2, 3, 4, 5]
    print(f"\nArray  : {arr1}")
    print(f"Target : 2  → Count (optimized): {count_occurrences(arr1, 2)}")
    print(f"Target : 2  → Count (brute)    : {count_occurrences_brute(arr1, 2)}")
    # Expected: 3

    # Test Case 2: Target not present
    print(f"\nTarget : 6  → Count (optimized): {count_occurrences(arr1, 6)}")
    # Expected: 0

    # Test Case 3: All elements are the target
    arr2 = [5, 5, 5, 5, 5]
    print(f"\nArray  : {arr2}")
    print(f"Target : 5  → Count: {count_occurrences(arr2, 5)}")   # Expected: 5

    # Test Case 4: Target appears once
    arr3 = [1, 2, 3, 4, 5]
    print(f"\nArray  : {arr3}")
    print(f"Target : 3  → Count: {count_occurrences(arr3, 3)}")   # Expected: 1

    # Test Case 5: Large array
    arr4 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
    print(f"\nArray  : {arr4}")
    print(f"Target : 4  → Count: {count_occurrences(arr4, 4)}")   # Expected: 4
    print(f"Target : 1  → Count: {count_occurrences(arr4, 1)}")   # Expected: 2

    # Test Case 6: Single element
    arr5 = [9]
    print(f"\nArray  : {arr5}")
    print(f"Target : 9  → Count: {count_occurrences(arr5, 9)}")   # Expected: 1
    print(f"Target : 1  → Count: {count_occurrences(arr5, 1)}")   # Expected: 0

    # Test Case 7: Empty array
    arr6 = []
    print(f"\nArray  : {arr6}")
    print(f"Target : 3  → Count: {count_occurrences(arr6, 3)}")   # Expected: 0

    print("\n" + "=" * 55)
