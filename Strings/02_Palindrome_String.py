"""
============================================================
Problem: Check if a String is a Palindrome
============================================================

Problem Statement:
    Given a string, determine whether it reads the same
    forwards and backwards (ignoring case and spaces).
    Return True if it is a palindrome, False otherwise.

Approach (Two-Pointer):
    - Normalize the string: convert to lowercase and strip
      spaces so that "Madam" and "A man a plan a canal Panama"
      are handled correctly.
    - Use two pointers: `left` at index 0 and `right` at the
      last index.
    - If characters at both pointers match, move them inward.
    - If they ever mismatch, return False immediately.
    - If the loop completes, return True.

    Alternative: Compare the string with its reverse (s == s[::-1]).
    The two-pointer approach is more interview-friendly as it
    avoids creating a reversed copy.

Time Complexity:  O(n) — at most n/2 comparisons.
Space Complexity: O(n) — O(n) for the normalized string.

Example:
    Input:  "racecar"
    Output: True

    Input:  "hello"
    Output: False
============================================================
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (case-insensitive, ignores spaces).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize: lowercase and remove spaces
    s = s.lower().replace(" ", "")

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False  # Mismatch found — not a palindrome
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Test Case 1: Classic palindrome
    s1 = "racecar"
    print(f"Input:        '{s1}'")
    print(f"Is Palindrome: {is_palindrome(s1)}")    # Expected: True

    print()

    # Test Case 2: Not a palindrome
    s2 = "hello"
    print(f"Input:        '{s2}'")
    print(f"Is Palindrome: {is_palindrome(s2)}")    # Expected: False

    print()

    # Test Case 3: Mixed case palindrome
    s3 = "Madam"
    print(f"Input:        '{s3}'")
    print(f"Is Palindrome: {is_palindrome(s3)}")    # Expected: True

    print()

    # Test Case 4: Palindrome with spaces
    s4 = "a man a plan a canal panama"
    print(f"Input:        '{s4}'")
    print(f"Is Palindrome: {is_palindrome(s4)}")    # Expected: True

    print()

    # Test Case 5: Single character (always a palindrome)
    s5 = "z"
    print(f"Input:        '{s5}'")
    print(f"Is Palindrome: {is_palindrome(s5)}")    # Expected: True

    print()

    # Test Case 6: Empty string (trivially a palindrome)
    s6 = ""
    print(f"Input:        '{s6}'")
    print(f"Is Palindrome: {is_palindrome(s6)}")    # Expected: True

    print()

    # Test Case 7: Two-character non-palindrome
    s7 = "ab"
    print(f"Input:        '{s7}'")
    print(f"Is Palindrome: {is_palindrome(s7)}")    # Expected: False
