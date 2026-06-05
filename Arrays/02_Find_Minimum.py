"""
============================================================
Problem: Find the Minimum Element in an Array
============================================================

Problem Statement:
    Given an array of integers, find and return the minimum
    (smallest) element present in the array.

Approach:
    - Initialize a variable `min_val` with the first element.
    - Iterate through the array starting from index 1.
    - If the current element is smaller than `min_val`, update it.
    - Return `min_val` after the loop ends.

Time Complexity:  O(n) — single pass through the array.
Space Complexity: O(1) — no extra space used.

Example:
    Input:  [3, 7, 1, 9, 4, 6]
    Output: 1
============================================================
"""


def find_minimum(arr: list) -> int:
    """
    Find the minimum element in a given array.

    Args:
        arr (list): A non-empty list of integers.

    Returns:
        int: The minimum element in the array.

    Raises:
        ValueError: If the array is empty.
    """
    if not arr:
        raise ValueError("Array must not be empty.")

    min_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num

    return min_val


if __name__ == "__main__":
    # Test Case 1: General case
    arr1 = [3, 7, 1, 9, 4, 6]
    print(f"Array:   {arr1}")
    print(f"Minimum: {find_minimum(arr1)}")   # Expected: 1

    print()

    # Test Case 2: Array with negative numbers
    arr2 = [-5, -1, -8, -3]
    print(f"Array:   {arr2}")
    print(f"Minimum: {find_minimum(arr2)}")   # Expected: -8

    print()

    # Test Case 3: Single element
    arr3 = [42]
    print(f"Array:   {arr3}")
    print(f"Minimum: {find_minimum(arr3)}")   # Expected: 42

    print()

    # Test Case 4: All elements same
    arr4 = [5, 5, 5, 5]
    print(f"Array:   {arr4}")
    print(f"Minimum: {find_minimum(arr4)}")   # Expected: 5
