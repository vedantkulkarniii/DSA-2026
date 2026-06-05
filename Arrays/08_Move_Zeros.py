"""
============================================================
Problem: Move All Zeros to the End of the Array
============================================================

Problem Statement:
    Given an array of integers, move all zeros to the end
    while maintaining the relative order of the non-zero
    elements. The operation must be performed in-place.

Approach (Two-Pointer / Write Index):
    - Use a `write_index` pointer starting at 0.
    - In the first pass, iterate through the array:
        - Every time a non-zero element is encountered,
          place it at arr[write_index] and increment write_index.
    - After the first pass, all non-zero elements are placed
      at the front in their original relative order.
    - In the second pass, fill the remaining positions from
      write_index to end with zeros.

    This guarantees in-place operation and preserves order.

Time Complexity:  O(n) — two passes through the array.
Space Complexity: O(1) — in-place modification, no extra space.

Example:
    Input:  [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
============================================================
"""


def move_zeros(arr: list) -> list:
    """
    Move all zeros to the end of the array in-place,
    while preserving the relative order of non-zero elements.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The modified array with zeros moved to the end.
    """
    write_index = 0

    # First pass: overwrite array positions with non-zero elements
    for num in arr:
        if num != 0:
            arr[write_index] = num
            write_index += 1

    # Second pass: fill remaining positions with zeros
    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1

    return arr


if __name__ == "__main__":
    # Test Case 1: General case
    arr1 = [0, 1, 0, 3, 12]
    print(f"Original: {arr1}")
    print(f"Result:   {move_zeros(arr1)}")   # Expected: [1, 3, 12, 0, 0]

    print()

    # Test Case 2: All zeros
    arr2 = [0, 0, 0, 0]
    print(f"Original: {arr2}")
    print(f"Result:   {move_zeros(arr2)}")   # Expected: [0, 0, 0, 0]

    print()

    # Test Case 3: No zeros
    arr3 = [1, 2, 3, 4]
    print(f"Original: {arr3}")
    print(f"Result:   {move_zeros(arr3)}")   # Expected: [1, 2, 3, 4]

    print()

    # Test Case 4: Zeros at the beginning
    arr4 = [0, 0, 1, 2, 3]
    print(f"Original: {arr4}")
    print(f"Result:   {move_zeros(arr4)}")   # Expected: [1, 2, 3, 0, 0]

    print()

    # Test Case 5: Single zero
    arr5 = [4, 0, 5]
    print(f"Original: {arr5}")
    print(f"Result:   {move_zeros(arr5)}")   # Expected: [4, 5, 0]

    print()

    # Test Case 6: Single element
    arr6 = [0]
    print(f"Original: {arr6}")
    print(f"Result:   {move_zeros(arr6)}")   # Expected: [0]
