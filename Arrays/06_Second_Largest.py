"""
============================================================
Problem: Find the Second Largest Element Without Sorting
============================================================

Problem Statement:
    Given an array of integers, find the second largest
    (second maximum) distinct element without sorting the
    array.

Approach:
    - Use two variables: `first` and `second`, both initialized
      to negative infinity.
    - Iterate through the array:
        - If the current element is greater than `first`,
          update `second = first` and `first = current`.
        - Else if the current element is greater than `second`
          and not equal to `first`, update `second`.
    - After the loop, if `second` is still negative infinity,
      no second largest exists (all elements are the same).

    This approach avoids sorting and does it in a single pass,
    which is optimal.

Time Complexity:  O(n) — single pass through the array.
Space Complexity: O(1) — only two extra variables used.

Example:
    Input:  [12, 35, 1, 10, 34, 1]
    Output: 34
============================================================
"""


def second_largest(arr: list):
    """
    Find the second largest distinct element in a given array.

    Args:
        arr (list): A list of integers with at least two distinct values.

    Returns:
        int | None: The second largest element, or None if it doesn't exist.

    Raises:
        ValueError: If the array has fewer than 2 elements.
    """
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements.")

    first = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        return None  # All elements are identical

    return second


if __name__ == "__main__":
    # Test Case 1: General case
    arr1 = [12, 35, 1, 10, 34, 1]
    print(f"Array:          {arr1}")
    print(f"Second Largest: {second_largest(arr1)}")   # Expected: 34

    print()

    # Test Case 2: Sorted array
    arr2 = [1, 2, 3, 4, 5]
    print(f"Array:          {arr2}")
    print(f"Second Largest: {second_largest(arr2)}")   # Expected: 4

    print()

    # Test Case 3: Duplicate largest values
    arr3 = [10, 10, 9, 8]
    print(f"Array:          {arr3}")
    print(f"Second Largest: {second_largest(arr3)}")   # Expected: 9

    print()

    # Test Case 4: All elements are the same
    arr4 = [7, 7, 7, 7]
    print(f"Array:          {arr4}")
    print(f"Second Largest: {second_largest(arr4)}")   # Expected: None

    print()

    # Test Case 5: Two elements
    arr5 = [100, 50]
    print(f"Array:          {arr5}")
    print(f"Second Largest: {second_largest(arr5)}")   # Expected: 50

    print()

    # Test Case 6: Negative numbers
    arr6 = [-1, -5, -3, -2]
    print(f"Array:          {arr6}")
    print(f"Second Largest: {second_largest(arr6)}")   # Expected: -2
