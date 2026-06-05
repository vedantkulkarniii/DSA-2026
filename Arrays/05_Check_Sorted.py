"""
============================================================
Problem: Check Whether an Array is Sorted in Ascending Order
============================================================

Problem Statement:
    Given an array of integers, determine whether the array
    is sorted in non-decreasing (ascending) order.
    Return True if sorted, False otherwise.

Approach:
    - Iterate through the array from index 0 to n-2.
    - At each step, compare arr[i] with arr[i+1].
    - If arr[i] > arr[i+1] at any point, the array is NOT
      sorted — return False immediately.
    - If the loop completes without finding any violation,
      return True.

    Note: An array with 0 or 1 element is considered sorted.

Time Complexity:  O(n) — single pass through the array.
Space Complexity: O(1) — no extra space used.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: True

    Input:  [1, 3, 2, 4, 5]
    Output: False
============================================================
"""


def is_sorted(arr: list) -> bool:
    """
    Check if a given array is sorted in ascending (non-decreasing) order.

    Args:
        arr (list): A list of integers.

    Returns:
        bool: True if sorted in ascending order, False otherwise.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


if __name__ == "__main__":
    # Test Case 1: Strictly sorted
    arr1 = [1, 2, 3, 4, 5]
    print(f"Array: {arr1}")
    print(f"Is Sorted: {is_sorted(arr1)}")   # Expected: True

    print()

    # Test Case 2: Not sorted
    arr2 = [1, 3, 2, 4, 5]
    print(f"Array: {arr2}")
    print(f"Is Sorted: {is_sorted(arr2)}")   # Expected: False

    print()

    # Test Case 3: Duplicate elements (non-decreasing is still sorted)
    arr3 = [1, 2, 2, 3, 4]
    print(f"Array: {arr3}")
    print(f"Is Sorted: {is_sorted(arr3)}")   # Expected: True

    print()

    # Test Case 4: Reverse sorted
    arr4 = [5, 4, 3, 2, 1]
    print(f"Array: {arr4}")
    print(f"Is Sorted: {is_sorted(arr4)}")   # Expected: False

    print()

    # Test Case 5: Single element
    arr5 = [10]
    print(f"Array: {arr5}")
    print(f"Is Sorted: {is_sorted(arr5)}")   # Expected: True

    print()

    # Test Case 6: Empty array
    arr6 = []
    print(f"Array: {arr6}")
    print(f"Is Sorted: {is_sorted(arr6)}")   # Expected: True
