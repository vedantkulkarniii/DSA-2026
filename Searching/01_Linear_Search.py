"""
============================================================
  DSA-2026 | Searching | Problem 01
  Topic   : Linear Search
  Author  : Vedant Kulkarni
  Updated : 2026
============================================================

Problem Statement:
    Given an unsorted (or sorted) array and a target value,
    find the index of the target using Linear Search.
    Return the index if found, otherwise return -1.

------------------------------------------------------------
Brute Force / Only Approach — Sequential Scan:
------------------------------------------------------------
    Linear Search IS the brute force approach. There is no
    smarter algorithm for an unsorted array.

    Steps:
    1. Start from index 0.
    2. Compare each element with the target.
    3. If a match is found, return the index immediately.
    4. If the loop ends without a match, return -1.

    Key Insight:
    - Works on both sorted and unsorted arrays.
    - No preprocessing required.
    - Optimal for small arrays or single searches.

------------------------------------------------------------
Complexity Analysis:
------------------------------------------------------------
    Time Complexity:
        Best Case  : O(1) — target is at index 0.
        Worst Case : O(n) — target is at the last index
                            or not present.
        Average    : O(n)

    Space Complexity: O(1) — no extra space used.

------------------------------------------------------------
When to Use Linear Search (Interview Tip):
------------------------------------------------------------
    - Array is unsorted.
    - Array is very small (n < 20).
    - You need to search only once (no repeated queries).
    - Searching in a Linked List (no random access).

------------------------------------------------------------
Example:
    Input : arr = [4, 2, 7, 1, 9, 3], target = 7
    Output: 2

    Input : arr = [4, 2, 7, 1, 9, 3], target = 5
    Output: -1
============================================================
"""


def linear_search(arr: list, target: int) -> int:
    """
    Search for target in arr using Linear Search.

    Args:
        arr    (list): List of integers (sorted or unsorted).
        target (int) : The value to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index        # Target found — return immediately

    return -1                   # Target not present in the array


def linear_search_all_occurrences(arr: list, target: int) -> list:
    """
    Return all indices where target appears in the array.

    Useful when duplicates exist and every occurrence is needed.

    Args:
        arr    (list): List of integers.
        target (int) : The value to search for.

    Returns:
        list: All indices where target is found (empty if none).
    """
    indices = []

    for index in range(len(arr)):
        if arr[index] == target:
            indices.append(index)

    return indices


if __name__ == "__main__":
    print("=" * 50)
    print("  Linear Search — Test Cases")
    print("=" * 50)

    # Test Case 1: Target found in the middle
    arr1 = [4, 2, 7, 1, 9, 3]
    print(f"\nArray  : {arr1}")
    print(f"Target : 7")
    print(f"Index  : {linear_search(arr1, 7)}")       # Expected: 2

    # Test Case 2: Target not present
    arr2 = [4, 2, 7, 1, 9, 3]
    print(f"\nArray  : {arr2}")
    print(f"Target : 5")
    print(f"Index  : {linear_search(arr2, 5)}")       # Expected: -1

    # Test Case 3: Target at index 0 (best case)
    arr3 = [10, 20, 30, 40]
    print(f"\nArray  : {arr3}")
    print(f"Target : 10")
    print(f"Index  : {linear_search(arr3, 10)}")      # Expected: 0

    # Test Case 4: Target at last index (worst case)
    arr4 = [10, 20, 30, 40]
    print(f"\nArray  : {arr4}")
    print(f"Target : 40")
    print(f"Index  : {linear_search(arr4, 40)}")      # Expected: 3

    # Test Case 5: Empty array
    arr5 = []
    print(f"\nArray  : {arr5}")
    print(f"Target : 1")
    print(f"Index  : {linear_search(arr5, 1)}")       # Expected: -1

    # Test Case 6: All occurrences (duplicates)
    arr6 = [3, 5, 3, 7, 3, 9]
    print(f"\nArray  : {arr6}")
    print(f"Target : 3")
    print(f"All Indices: {linear_search_all_occurrences(arr6, 3)}")
    # Expected: [0, 2, 4]

    # Test Case 7: Single element — found
    arr7 = [42]
    print(f"\nArray  : {arr7}")
    print(f"Target : 42")
    print(f"Index  : {linear_search(arr7, 42)}")      # Expected: 0

    print("\n" + "=" * 50)
