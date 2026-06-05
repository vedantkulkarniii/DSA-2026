"""
============================================================
Problem: Remove Duplicates from a Sorted Array
============================================================

Problem Statement:
    Given a sorted array of integers, remove the duplicate
    elements in-place such that each unique element appears
    only once. Return the new length of the array after
    removing duplicates.

    Note: The input array is already sorted, which means
    duplicate elements are always adjacent.

Approach (Two-Pointer):
    - Use a slow pointer `write_index` starting at 1.
    - Use a fast pointer `i` to iterate from index 1 onward.
    - If arr[i] != arr[i-1], it's a new unique element:
        - Place it at arr[write_index] and increment write_index.
    - After the loop, arr[:write_index] contains all unique elements.

    This is optimal because the array is already sorted,
    so duplicates are always adjacent.

Time Complexity:  O(n) — single pass through the array.
Space Complexity: O(1) — in-place modification, no extra space.

Example:
    Input:  [1, 1, 2, 3, 3, 4, 5, 5]
    Output: Length = 5, Unique Array = [1, 2, 3, 4, 5]
============================================================
"""


def remove_duplicates(arr: list) -> int:
    """
    Remove duplicates from a sorted array in-place.

    Args:
        arr (list): A sorted list of integers.

    Returns:
        int: The number of unique elements. The first `k`
             elements of `arr` will hold the unique values.
    """
    if not arr:
        return 0

    write_index = 1  # Position to place the next unique element

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index


if __name__ == "__main__":
    # Test Case 1: General case with multiple duplicates
    arr1 = [1, 1, 2, 3, 3, 4, 5, 5]
    print(f"Original Array: {arr1}")
    k1 = remove_duplicates(arr1)
    print(f"Unique Length:  {k1}")           # Expected: 5
    print(f"Unique Array:   {arr1[:k1]}")    # Expected: [1, 2, 3, 4, 5]

    print()

    # Test Case 2: No duplicates
    arr2 = [1, 2, 3, 4, 5]
    print(f"Original Array: {arr2}")
    k2 = remove_duplicates(arr2)
    print(f"Unique Length:  {k2}")           # Expected: 5
    print(f"Unique Array:   {arr2[:k2]}")    # Expected: [1, 2, 3, 4, 5]

    print()

    # Test Case 3: All duplicates
    arr3 = [7, 7, 7, 7]
    print(f"Original Array: {arr3}")
    k3 = remove_duplicates(arr3)
    print(f"Unique Length:  {k3}")           # Expected: 1
    print(f"Unique Array:   {arr3[:k3]}")    # Expected: [7]

    print()

    # Test Case 4: Empty array
    arr4 = []
    print(f"Original Array: {arr4}")
    k4 = remove_duplicates(arr4)
    print(f"Unique Length:  {k4}")           # Expected: 0

    print()

    # Test Case 5: Single element
    arr5 = [3]
    print(f"Original Array: {arr5}")
    k5 = remove_duplicates(arr5)
    print(f"Unique Length:  {k5}")           # Expected: 1
    print(f"Unique Array:   {arr5[:k5]}")    # Expected: [3]
