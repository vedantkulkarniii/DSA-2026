"""
============================================================
Problem: Find the Maximum Element in an Array
============================================================

Problem Statement:
    Given an array of integers, find and return the maximum
    (largest) element present in the array.

Approach:
    - Initialize a variable `max_val` with the first element.
    - Iterate through the array starting from index 1.
    - If the current element is greater than `max_val`, update it.
    - Return `max_val` after the loop ends.

Time Complexity:  O(n) — single pass through the array.
Space Complexity: O(1) — no extra space used.

Example:
    Input:  [3, 7, 1, 9, 4, 6]
    Output: 9
============================================================
"""


def find_maximum(arr: list) -> int:
    """
    Find the maximum element in a given array.

    Args:
        arr (list): A non-empty list of integers.

    Returns:
        int: The maximum element in the array.

    Raises:
        ValueError: If the array is empty.
    """
    if not arr:
        raise ValueError("Array must not be empty.")

    max_val = arr[0]

    for num in arr[1:]:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    # Test Case 1: General case
    arr1 = [3, 7, 1, 9, 4, 6]
    print(f"Array:   {arr1}")
    print(f"Maximum: {find_maximum(arr1)}")   # Expected: 9

    print()

    # Test Case 2: Array with negative numbers
    arr2 = [-5, -1, -8, -3]
    print(f"Array:   {arr2}")
    print(f"Maximum: {find_maximum(arr2)}")   # Expected: -1

    print()

    # Test Case 3: Single element
    arr3 = [42]
    print(f"Array:   {arr3}")
    print(f"Maximum: {find_maximum(arr3)}")   # Expected: 42

    print()

    # Test Case 4: All elements same
    arr4 = [5, 5, 5, 5]
    print(f"Array:   {arr4}")
    print(f"Maximum: {find_maximum(arr4)}")   # Expected: 5
