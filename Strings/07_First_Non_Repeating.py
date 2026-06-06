"""
============================================================
Problem: Find the First Non-Repeating Character in a String
============================================================

Problem Statement:
    Given a string, find the first character that does not
    repeat (appears exactly once). Return the character and
    its index. If all characters repeat, return None.

Approach (Two-Pass Hash Map):
    - Pass 1: Build a frequency dictionary — count occurrences
      of every character in the string.
    - Pass 2: Iterate through the string in order and return
      the first character whose frequency is exactly 1.

    Why two passes?
    - We need to know the frequency of ALL characters before
      we can determine which is the first non-repeating one.
    - A single-pass approach cannot know if a character seen
      once will repeat later.

    The second pass preserves the original order, which is
    crucial for "first" non-repeating.

Time Complexity:  O(n) — two O(n) passes = O(2n) = O(n).
Space Complexity: O(k) — k unique characters in the string
                         (at most O(1) for a fixed alphabet).

Example:
    Input:  "leetcode"
    Output: 'l' at index 0

    Input:  "aabb"
    Output: None (no non-repeating character)
============================================================
"""


def first_non_repeating(s: str):
    """
    Find the first non-repeating character in a string.

    Args:
        s (str): The input string.

    Returns:
        tuple | None: A tuple (char, index) of the first
                      non-repeating character, or None if
                      all characters repeat.
    """
    if not s:
        return None

    # Pass 1: Build frequency map
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Pass 2: Find first character with frequency == 1
    for index, char in enumerate(s):
        if freq[char] == 1:
            return char, index

    return None  # All characters repeat


if __name__ == "__main__":
    # Test Case 1: Standard case
    s1 = "leetcode"
    result1 = first_non_repeating(s1)
    print(f"Input:  '{s1}'")
    if result1:
        print(f"First Non-Repeating: '{result1[0]}' at index {result1[1]}")
    else:
        print("No non-repeating character found.")
    # Expected: 'l' at index 0

    print()

    # Test Case 2: Non-repeating at the end
    s2 = "aabbccd"
    result2 = first_non_repeating(s2)
    print(f"Input:  '{s2}'")
    if result2:
        print(f"First Non-Repeating: '{result2[0]}' at index {result2[1]}")
    else:
        print("No non-repeating character found.")
    # Expected: 'd' at index 6

    print()

    # Test Case 3: All characters repeat
    s3 = "aabb"
    result3 = first_non_repeating(s3)
    print(f"Input:  '{s3}'")
    if result3:
        print(f"First Non-Repeating: '{result3[0]}' at index {result3[1]}")
    else:
        print("No non-repeating character found.")
    # Expected: None

    print()

    # Test Case 4: Single character
    s4 = "z"
    result4 = first_non_repeating(s4)
    print(f"Input:  '{s4}'")
    if result4:
        print(f"First Non-Repeating: '{result4[0]}' at index {result4[1]}")
    else:
        print("No non-repeating character found.")
    # Expected: 'z' at index 0

    print()

    # Test Case 5: Non-repeating in the middle
    s5 = "aabcbb"
    result5 = first_non_repeating(s5)
    print(f"Input:  '{s5}'")
    if result5:
        print(f"First Non-Repeating: '{result5[0]}' at index {result5[1]}")
    else:
        print("No non-repeating character found.")
    # Expected: 'c' at index 3

    print()

    # Test Case 6: Empty string
    s6 = ""
    result6 = first_non_repeating(s6)
    print(f"Input:  '{s6}'")
    print(f"Result: {result6}")
    # Expected: None
