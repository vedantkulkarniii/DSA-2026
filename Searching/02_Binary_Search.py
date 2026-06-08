"""
============================================================
  DSA-2026 | Searching | Problem 02
  Topic   : Binary Search
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given a SORTED array of integers and a target value,
    implement Binary Search and return the index of the
    target. Return -1 if the target is not found.

------------------------------------------------------------
Brute Force — Linear Search:
------------------------------------------------------------
    Simply scan from left to right: O(n) time.
    Inefficient for large sorted arrays.

------------------------------------------------------------
Optimized Approach — Binary Search (Divide and Conquer):
------------------------------------------------------------
    Prerequisite: Array MUST be sorted.

    Core Idea:
    - At every step, examine the middle element.
    - If middle == target  → found, return mid.
    - If middle < target   → target is in the RIGHT half,
                             discard the left half.
    - If middle > target   → target is in the LEFT half,
                             discard the right half.
    - Repeat until the search space is empty.

    This halves the search space at each step, giving
    logarithmic time complexity.

    Mid Calculation:
        mid = left + (right - left) // 2
        (Avoids integer overflow vs (left + right) // 2)

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity:
        Best Case  : O(1)      — target is at the midpoint.
        Worst Case : O(log n)  — target not found or at edge.
        Average    : O(log n)

    Space Complexity:
        Iterative : O(1) — no extra space.
        Recursive : O(log n) — call stack depth.

------------------------------------------------------------
Iterative vs Recursive (Interview Tip):
------------------------------------------------------------
    - Iterative is preferred in interviews (avoids stack overhead).
    - Recursive is cleaner and easier to reason about.
    - Both are shown below.

------------------------------------------------------------
Example:
    Input : arr = [1, 3, 5, 7, 9, 11, 13], target = 7
    Output: 3

    Input : arr = [1, 3, 5, 7, 9, 11, 13], target = 6
    Output: -1
============================================================
"""


def binary_search_iterative(arr: list, target: int) -> int:
    """
    Binary Search — Iterative implementation.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The value to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Safe mid calculation to prevent integer overflow
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid                  # Target found

        elif arr[mid] < target:
            left = mid + 1              # Target is in the right half

        else:
            right = mid - 1             # Target is in the left half

    return -1                           # Target not found


def binary_search_recursive(arr: list, target: int,
                             left: int, right: int) -> int:
    """
    Binary Search — Recursive implementation.

    Args:
        arr    (list): A sorted list of integers.
        target (int) : The value to search for.
        left   (int) : Left boundary of current search space.
        right  (int) : Right boundary of current search space.

    Returns:
        int: Index of target if found, else -1.
    """
    # Base case: search space exhausted
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid                              # Target found

    elif arr[mid] < target:
        return binary_search_recursive(         # Search right half
            arr, target, mid + 1, right
        )
    else:
        return binary_search_recursive(         # Search left half
            arr, target, left, mid - 1
        )


if __name__ == "__main__":
    print("=" * 55)
    print("  Binary Search — Test Cases")
    print("=" * 55)

    arr = [1, 3, 5, 7, 9, 11, 13]
    print(f"\nArray: {arr}")

    # Test Case 1: Target in the middle
    t1 = 7
    print(f"\nTarget: {t1}")
    print(f"Iterative : {binary_search_iterative(arr, t1)}")            # 3
    print(f"Recursive : {binary_search_recursive(arr, t1, 0, len(arr)-1)}")  # 3

    # Test Case 2: Target not present
    t2 = 6
    print(f"\nTarget: {t2}")
    print(f"Iterative : {binary_search_iterative(arr, t2)}")            # -1
    print(f"Recursive : {binary_search_recursive(arr, t2, 0, len(arr)-1)}")  # -1

    # Test Case 3: Target at first index
    t3 = 1
    print(f"\nTarget: {t3}")
    print(f"Iterative : {binary_search_iterative(arr, t3)}")            # 0
    print(f"Recursive : {binary_search_recursive(arr, t3, 0, len(arr)-1)}")  # 0

    # Test Case 4: Target at last index
    t4 = 13
    print(f"\nTarget: {t4}")
    print(f"Iterative : {binary_search_iterative(arr, t4)}")            # 6
    print(f"Recursive : {binary_search_recursive(arr, t4, 0, len(arr)-1)}")  # 6

    # Test Case 5: Single element — found
    arr2 = [42]
    t5 = 42
    print(f"\nArray: {arr2}, Target: {t5}")
    print(f"Iterative : {binary_search_iterative(arr2, t5)}")           # 0

    # Test Case 6: Single element — not found
    t6 = 10
    print(f"\nArray: {arr2}, Target: {t6}")
    print(f"Iterative : {binary_search_iterative(arr2, t6)}")           # -1

    # Test Case 7: Empty array
    arr3 = []
    t7 = 5
    print(f"\nArray: {arr3}, Target: {t7}")
    print(f"Iterative : {binary_search_iterative(arr3, t7)}")           # -1

    print("\n" + "=" * 55)
