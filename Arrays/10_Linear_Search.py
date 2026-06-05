"""
============================================================
Problem: Linear Search — Find Target Element and Return Index
============================================================

Problem Statement:
    Given an array of integers and a target value, search
    for the target element using linear search and return
    its index. If the target is not found, return -1.

Approach:
    - Iterate through the array from left to right.
    - At each index, compare the current element with target.
    - If a match is found, return the current index immediately.
    - If the loop ends without finding the target, return -1.

    Linear Search is the simplest search algorithm and works
    on both sorted and unsorted arrays. It is preferred when:
    - The array is unsorted.
    - The array is small.
    - We only need to search once (no preprocessing worthwhile).

Time Complexity:
    - Best Case:    O(1) — target is at the first position.
    - Worst Case:   O(n) — target is at the last position or absent.
    - Average Case: O(n)

Space Complexity: O(1) — no extra space used.

Example:
    Input:  arr = [4, 2, 7, 1, 9, 3], target = 7
    Output: 2  (index of element 7)

    Input:  arr = [4, 2, 7, 1, 9, 3], target = 5
    Output: -1 (not found)
============================================================
"""


def linear_search(arr: list, target: int) -> int:
    """
    Search for a target element in the array using linear search.

    Args:
        arr (list): A list of integers (sorted or unsorted).
        target (int): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index

    return -1  # Target not found


if __name__ == "__main__":
    # Test Case 1: Target found in the middle
    arr1 = [4, 2, 7, 1, 9, 3]
    target1 = 7
    result1 = linear_search(arr1, target1)
    print(f"Array:  {arr1}")
    print(f"Target: {target1}")
    print(f"Index:  {result1}")   # Expected: 2

    print()

    # Test Case 2: Target not found
    arr2 = [4, 2, 7, 1, 9, 3]
    target2 = 5
    result2 = linear_search(arr2, target2)
    print(f"Array:  {arr2}")
    print(f"Target: {target2}")
    print(f"Index:  {result2}")   # Expected: -1

    print()

    # Test Case 3: Target at the first position
    arr3 = [10, 20, 30, 40]
    target3 = 10
    result3 = linear_search(arr3, target3)
    print(f"Array:  {arr3}")
    print(f"Target: {target3}")
    print(f"Index:  {result3}")   # Expected: 0

    print()

    # Test Case 4: Target at the last position
    arr4 = [10, 20, 30, 40]
    target4 = 40
    result4 = linear_search(arr4, target4)
    print(f"Array:  {arr4}")
    print(f"Target: {target4}")
    print(f"Index:  {result4}")   # Expected: 3

    print()

    # Test Case 5: Empty array
    arr5 = []
    target5 = 1
    result5 = linear_search(arr5, target5)
    print(f"Array:  {arr5}")
    print(f"Target: {target5}")
    print(f"Index:  {result5}")   # Expected: -1

    print()

    # Test Case 6: Duplicate elements (returns first occurrence)
    arr6 = [3, 5, 3, 7, 3]
    target6 = 3
    result6 = linear_search(arr6, target6)
    print(f"Array:  {arr6}")
    print(f"Target: {target6}")
    print(f"Index:  {result6}")   # Expected: 0 (first occurrence)
