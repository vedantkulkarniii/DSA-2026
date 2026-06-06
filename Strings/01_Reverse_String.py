"""
============================================================
Problem: Reverse a String
============================================================

Problem Statement:
    Given a string, return it in reversed order.
    For example, "hello" becomes "olleh".

Approach (Two-Pointer):
    - Convert the string to a list of characters (strings
      are immutable in Python).
    - Use two pointers: `left` at index 0 and `right` at
      the last index.
    - Swap characters at both pointers and move them inward
      until they meet.
    - Join the list back into a string and return it.

    This is the classic in-place two-pointer reversal.
    Python also supports slicing (s[::-1]), shown as an
    alternative in the test block.

Time Complexity:  O(n) — we traverse half the string.
Space Complexity: O(n) — O(n) for the character list
                         (strings are immutable in Python).

Example:
    Input:  "hello"
    Output: "olleh"
============================================================
"""


def reverse_string(s: str) -> str:
    """
    Reverse a string using the two-pointer technique.

    Args:
        s (str): The input string to reverse.

    Returns:
        str: The reversed string.
    """
    # Convert to list because strings are immutable in Python
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        # Swap characters at left and right pointers
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    # Test Case 1: General case
    s1 = "hello"
    print(f"Input:    '{s1}'")
    print(f"Reversed: '{reverse_string(s1)}'")    # Expected: 'olleh'

    print()

    # Test Case 2: Palindrome (should look the same)
    s2 = "madam"
    print(f"Input:    '{s2}'")
    print(f"Reversed: '{reverse_string(s2)}'")    # Expected: 'madam'

    print()

    # Test Case 3: Single character
    s3 = "a"
    print(f"Input:    '{s3}'")
    print(f"Reversed: '{reverse_string(s3)}'")    # Expected: 'a'

    print()

    # Test Case 4: String with spaces
    s4 = "Data Structures"
    print(f"Input:    '{s4}'")
    print(f"Reversed: '{reverse_string(s4)}'")    # Expected: 'serutcurtS ataD'

    print()

    # Test Case 5: Empty string
    s5 = ""
    print(f"Input:    '{s5}'")
    print(f"Reversed: '{reverse_string(s5)}'")    # Expected: ''

    print()

    # Alternative: Python slicing (one-liner)
    s6 = "python"
    print(f"Input (slicing):    '{s6}'")
    print(f"Reversed (slicing): '{s6[::-1]}'")    # Expected: 'nohtyp'
