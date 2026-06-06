"""
============================================================
Problem: Check if Two Strings are Anagrams
============================================================

Problem Statement:
    Given two strings, determine whether they are anagrams
    of each other. Two strings are anagrams if one can be
    formed by rearranging the letters of the other.
    The check is case-insensitive and ignores spaces.

    Example:
        "listen" and "silent"  → True  (same letters, different order)
        "hello"  and "world"   → False (different letters)

Approach (Frequency Count / Hash Map):
    - Normalize both strings: lowercase and remove spaces.
    - If their lengths differ after normalization, they
      cannot be anagrams — return False early.
    - Build a frequency dictionary for the first string.
    - For the second string, decrement counts from the dict.
    - If any character count goes negative, return False.
    - If all counts end at 0, return True.

    Alternative: Sort both strings and compare (O(n log n)).
    The frequency map approach is optimal at O(n).

Time Complexity:  O(n) — two passes, one per string.
Space Complexity: O(k) — k unique characters in the alphabet.

Example:
    Input:  "listen", "silent"
    Output: True

    Input:  "hello", "world"
    Output: False
============================================================
"""


def are_anagrams(s1: str, s2: str) -> bool:
    """
    Check whether two strings are anagrams of each other.

    The comparison is case-insensitive and ignores spaces.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Normalize: lowercase and remove spaces
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    # Quick length check — anagrams must have equal lengths
    if len(s1) != len(s2):
        return False

    # Build frequency map for s1
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1

    # Decrement counts using characters from s2
    for char in s2:
        if char not in freq:
            return False   # s2 has a character not in s1
        freq[char] -= 1
        if freq[char] < 0:
            return False   # s2 has more of this character than s1

    return True


if __name__ == "__main__":
    # Test Case 1: Classic anagram pair
    s1, s2 = "listen", "silent"
    print(f"'{s1}' and '{s2}'")
    print(f"Are Anagrams: {are_anagrams(s1, s2)}")    # Expected: True

    print()

    # Test Case 2: Not anagrams
    s3, s4 = "hello", "world"
    print(f"'{s3}' and '{s4}'")
    print(f"Are Anagrams: {are_anagrams(s3, s4)}")    # Expected: False

    print()

    # Test Case 3: Case-insensitive check
    s5, s6 = "Triangle", "Integral"
    print(f"'{s5}' and '{s6}'")
    print(f"Are Anagrams: {are_anagrams(s5, s6)}")    # Expected: True

    print()

    # Test Case 4: Anagram with spaces
    s7, s8 = "Astronomer", "Moon starer"
    print(f"'{s7}' and '{s8}'")
    print(f"Are Anagrams: {are_anagrams(s7, s8)}")    # Expected: True

    print()

    # Test Case 5: Different lengths
    s9, s10 = "abc", "ab"
    print(f"'{s9}' and '{s10}'")
    print(f"Are Anagrams: {are_anagrams(s9, s10)}")   # Expected: False

    print()

    # Test Case 6: Same string
    s11, s12 = "python", "python"
    print(f"'{s11}' and '{s12}'")
    print(f"Are Anagrams: {are_anagrams(s11, s12)}")  # Expected: True

    print()

    # Test Case 7: Empty strings
    s13, s14 = "", ""
    print(f"'{s13}' and '{s14}'")
    print(f"Are Anagrams: {are_anagrams(s13, s14)}")  # Expected: True
