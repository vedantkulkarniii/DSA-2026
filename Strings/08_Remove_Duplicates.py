"""
============================================================
Problem: Remove Duplicate Characters from a String
============================================================

Problem Statement:
    Given a string, remove all duplicate characters and return
    a new string containing only the first occurrence of each
    character, preserving the original order.

    Example:
        "programming" → "progamin"
        "aabbcc"      → "abc"

Approach (Seen Set + Result List):
    - Use a set `seen` to track characters already encountered.
    - Use a list `result` to build the output in order.
    - Iterate through the string:
        - If the character is NOT in `seen`, add it to both
          `seen` and `result`.
        - If it IS in `seen`, skip it (it's a duplicate).
    - Join `result` into a string and return.

    The set provides O(1) average-case lookup, making the
    overall algorithm linear. A list is used for `result`
    because string concatenation (+=) is O(n) per step.

Time Complexity:  O(n) — single pass through the string.
Space Complexity: O(k) — k unique characters stored in set
                         and result list.

Example:
    Input:  "programming"
    Output: "progamin"
============================================================
"""


def remove_duplicates(s: str) -> str:
    """
    Remove duplicate characters from a string, keeping the
    first occurrence of each character in original order.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with duplicate characters removed.
    """
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
        # Duplicate — skip this character

    return "".join(result)


if __name__ == "__main__":
    # Test Case 1: Standard string with duplicates
    s1 = "programming"
    print(f"Input:  '{s1}'")
    print(f"Output: '{remove_duplicates(s1)}'")    # Expected: 'progamin'

    print()

    # Test Case 2: All duplicates
    s2 = "aabbcc"
    print(f"Input:  '{s2}'")
    print(f"Output: '{remove_duplicates(s2)}'")    # Expected: 'abc'

    print()

    # Test Case 3: No duplicates
    s3 = "abcdef"
    print(f"Input:  '{s3}'")
    print(f"Output: '{remove_duplicates(s3)}'")    # Expected: 'abcdef'

    print()

    # Test Case 4: All same characters
    s4 = "aaaaa"
    print(f"Input:  '{s4}'")
    print(f"Output: '{remove_duplicates(s4)}'")    # Expected: 'a'

    print()

    # Test Case 5: String with spaces (spaces are also characters)
    s5 = "hello world"
    print(f"Input:  '{s5}'")
    print(f"Output: '{remove_duplicates(s5)}'")    # Expected: 'helo wrd'

    print()

    # Test Case 6: Mixed case (case-sensitive by default)
    s6 = "AaBbCc"
    print(f"Input:  '{s6}'")
    print(f"Output: '{remove_duplicates(s6)}'")    # Expected: 'AaBbCc' (all unique)

    print()

    # Test Case 7: Empty string
    s7 = ""
    print(f"Input:  '{s7}'")
    print(f"Output: '{remove_duplicates(s7)}'")    # Expected: ''

    print()

    # Test Case 8: Single character
    s8 = "x"
    print(f"Input:  '{s8}'")
    print(f"Output: '{remove_duplicates(s8)}'")    # Expected: 'x'
