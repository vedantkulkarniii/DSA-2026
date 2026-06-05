"""
============================================================
Problem: Calculate the Sum of All Elements in an Array
============================================================

Problem Statement:
    Given an array of integers, calculate and return the
    sum of all its elements.

Approach:
    - Initialize a variable `total` to 0.
    - Iterate through every element of the array.
    - Add each element to `total`.
    - Return `total` after the loop ends.

Time Complexity:  O(n) — single pass through the array.
Space Complexity: O(1) — no extra space used.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: 15
============================================================
"""


def array_sum(arr: list) -> int:
    """
    Calculate the sum of all elements in a given array.

    Args:
        arr (list): A list of integers (can be empty).

    Returns:
        int: The sum of all elements. Returns 0 for an empty array.
    """
    total = 0

    for num in arr:
        total += num

    return total


if __name__ == "__main__":
    # Test Case 1: General case
    arr1 = [1, 2, 3, 4, 5]
    print(f"Array: {arr1}")
    print(f"Sum:   {array_sum(arr1)}")   # Expected: 15

    print()

    # Test Case 2: Array with negative numbers
    arr2 = [10, -3, 7, -2, 5]
    print(f"Array: {arr2}")
    print(f"Sum:   {array_sum(arr2)}")   # Expected: 17

    print()

    # Test Case 3: Empty array
    arr3 = []
    print(f"Array: {arr3}")
    print(f"Sum:   {array_sum(arr3)}")   # Expected: 0

    print()

    # Test Case 4: Single element
    arr4 = [99]
    print(f"Array: {arr4}")
    print(f"Sum:   {array_sum(arr4)}")   # Expected: 99

    print()

    # Test Case 5: All zeros
    arr5 = [0, 0, 0, 0]
    print(f"Array: {arr5}")
    print(f"Sum:   {array_sum(arr5)}")   # Expected: 0
