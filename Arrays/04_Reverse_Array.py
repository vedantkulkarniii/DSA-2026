"""
============================================================
Problem: Reverse an Array Using the Two-Pointer Approach
============================================================

Problem Statement:
    Given an array of integers, reverse it in-place using
    the two-pointer technique without using extra space.

Approach (Two-Pointer):
    - Use two pointers: `left` starting at index 0 and
      `right` starting at the last index (len(arr) - 1).
    - Swap arr[left] and arr[right].
    - Move `left` forward and `right` backward.
    - Repeat until `left` >= `right`.

    This approach is more efficient than creating a new
    reversed list as it works in-place.

Time Complexity:  O(n) — we traverse half the array.
Space Complexity: O(1) — in-place reversal, no extra space.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
============================================================
"""


def reverse_array(arr: list) -> list:
    """
    Reverse an array in-place using the two-pointer approach.

    Args:
        arr (list): A list of integers.

    Returns:
        list: The same list reversed in-place.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    # Test Case 1: Odd number of elements
    arr1 = [1, 2, 3, 4, 5]
    print(f"Original: {arr1}")
    print(f"Reversed: {reverse_array(arr1)}")   # Expected: [5, 4, 3, 2, 1]

    print()

    # Test Case 2: Even number of elements
    arr2 = [10, 20, 30, 40]
    print(f"Original: {arr2}")
    print(f"Reversed: {reverse_array(arr2)}")   # Expected: [40, 30, 20, 10]

    print()

    # Test Case 3: Single element
    arr3 = [7]
    print(f"Original: {arr3}")
    print(f"Reversed: {reverse_array(arr3)}")   # Expected: [7]

    print()

    # Test Case 4: Two elements
    arr4 = [1, 2]
    print(f"Original: {arr4}")
    print(f"Reversed: {reverse_array(arr4)}")   # Expected: [2, 1]

    print()

    # Test Case 5: Already reversed
    arr5 = [5, 4, 3, 2, 1]
    print(f"Original: {arr5}")
    print(f"Reversed: {reverse_array(arr5)}")   # Expected: [1, 2, 3, 4, 5]
