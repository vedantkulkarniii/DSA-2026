"""
============================================================
Problem: Convert a String to Uppercase (Manual Implementation)
============================================================

Problem Statement:
    Given a string, convert all lowercase letters to their
    uppercase equivalents without using the built-in
    str.upper() method.

    This problem teaches ASCII-based character manipulation,
    a common concept in low-level programming and interviews.

Approach (ASCII Manipulation):
    - In ASCII, lowercase letters 'a' to 'z' have values 97–122.
    - Uppercase letters 'A' to 'Z' have values 65–90.
    - The difference between a lowercase and its uppercase
      equivalent is always 32 (e.g., ord('a') - ord('A') = 32).
    - For each character:
        - If it is a lowercase letter (ord value between 97–122),
          subtract 32 from its ASCII value and convert back
          to a character using chr().
        - Otherwise, keep the character as-is.
    - Join all characters and return the result.

Time Complexity:  O(n) — single pass through the string.
Space Complexity: O(n) — new string/list to store result.

Example:
    Input:  "hello world"
    Output: "HELLO WORLD"
============================================================
"""


def to_uppercase(s: str) -> str:
    """
    Convert all lowercase letters in a string to uppercase
    using ASCII manipulation (without str.upper()).

    Args:
        s (str): The input string.

    Returns:
        str: The string with all lowercase letters converted
             to uppercase. Other characters remain unchanged.
    """
    result = []

    for char in s:
        # Check if the character is a lowercase letter using ASCII range
        if 'a' <= char <= 'z':
            # Subtract 32 to convert lowercase to uppercase via ASCII
            result.append(chr(ord(char) - 32))
        else:
            # Non-lowercase characters remain unchanged
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    # Test Case 1: All lowercase
    s1 = "hello world"
    print(f"Input:     '{s1}'")
    print(f"Uppercase: '{to_uppercase(s1)}'")    # Expected: 'HELLO WORLD'

    print()

    # Test Case 2: Mixed case
    s2 = "Python Programming"
    print(f"Input:     '{s2}'")
    print(f"Uppercase: '{to_uppercase(s2)}'")    # Expected: 'PYTHON PROGRAMMING'

    print()

    # Test Case 3: Already uppercase
    s3 = "ALREADY UPPER"
    print(f"Input:     '{s3}'")
    print(f"Uppercase: '{to_uppercase(s3)}'")    # Expected: 'ALREADY UPPER'

    print()

    # Test Case 4: String with digits and symbols
    s4 = "dsa-2026!"
    print(f"Input:     '{s4}'")
    print(f"Uppercase: '{to_uppercase(s4)}'")    # Expected: 'DSA-2026!'

    print()

    # Test Case 5: Empty string
    s5 = ""
    print(f"Input:     '{s5}'")
    print(f"Uppercase: '{to_uppercase(s5)}'")    # Expected: ''

    print()

    # Test Case 6: Single lowercase character
    s6 = "a"
    print(f"Input:     '{s6}'")
    print(f"Uppercase: '{to_uppercase(s6)}'")    # Expected: 'A'

    print()

    # Verification against built-in
    test = "verify with builtin"
    match = to_uppercase(test) == test.upper()
    print(f"Matches str.upper(): {match}")       # Expected: True
