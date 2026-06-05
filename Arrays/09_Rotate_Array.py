"""
============================================================
Problem: Rotate an Array by One Position to the Right
============================================================

Problem Statement:
    Given an array of integers, rotate it to the right by
    one position. The last element should move to the front,
    and all other elements should shift one position to the right.

Approach:
    - Store the last element in a temporary variable `last`.
    - Shift all elements from index n-2 down to 0 one position
      to the right (i.e., arr[i+1] = arr[i]).
    - Place `last` at index 0.

    Alternative Approach (Reversal):
    - Reverse the entire array.
    - Reverse the first element.
    - Reverse the remaining elements.
    (The iterative shift approach is used here for clarity.)

Time Complexity:  O(n) — single pass to shift elements.
Space Complexity: O(1) — only one extra variable (`last`).

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: [5, 1, 2, 3, 4]
============================================================
"""


def rotate_right_by_one(arr: list) -> list:
    """
    Rotate an array to the right by one position.

    The last element becomes the first, and all other elements
    shift one position to the right.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The rotated array (modified in-place).
    """
    if len(arr) <= 1:
        return arr

    # Save the last element
    last = arr[-1]

    # Shift all elements one position to the right
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Place the last element at the beginning
    arr[0] = last

    return arr


if __name__ == "__main__":
    # Test Case 1: General case
    arr1 = [1, 2, 3, 4, 5]
    print(f"Original: {arr1}")
    print(f"Rotated:  {rotate_right_by_one(arr1)}")   # Expected: [5, 1, 2, 3, 4]

    print()

    # Test Case 2: Two elements
    arr2 = [10, 20]
    print(f"Original: {arr2}")
    print(f"Rotated:  {rotate_right_by_one(arr2)}")   # Expected: [20, 10]

    print()

    # Test Case 3: Single element
    arr3 = [7]
    print(f"Original: {arr3}")
    print(f"Rotated:  {rotate_right_by_one(arr3)}")   # Expected: [7]

    print()

    # Test Case 4: Array with duplicate values
    arr4 = [1, 1, 2, 2, 3]
    print(f"Original: {arr4}")
    print(f"Rotated:  {rotate_right_by_one(arr4)}")   # Expected: [3, 1, 1, 2, 2]

    print()

    # Test Case 5: Already rotated once
    arr5 = [5, 1, 2, 3, 4]
    print(f"Original: {arr5}")
    print(f"Rotated:  {rotate_right_by_one(arr5)}")   # Expected: [4, 5, 1, 2, 3]
