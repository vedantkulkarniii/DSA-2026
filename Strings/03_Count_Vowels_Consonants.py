"""
============================================================
Problem: Count Vowels and Consonants in a String
============================================================

Problem Statement:
    Given a string, count the number of vowels (a, e, i, o, u)
    and consonants (all other alphabetic characters) in it.
    Non-alphabetic characters (digits, spaces, punctuation)
    should be ignored.

Approach:
    - Define a set of vowels for O(1) lookup: {'a','e','i','o','u'}.
    - Convert the string to lowercase for uniform comparison.
    - Iterate through each character:
        - If it is alphabetic (isalpha()), check if it is a vowel
          or consonant and increment the respective counter.
        - Skip non-alphabetic characters entirely.
    - Return a tuple (vowel_count, consonant_count).

    Using a set for vowel lookup ensures O(1) membership check
    rather than O(k) with a list.

Time Complexity:  O(n) — single pass through the string.
Space Complexity: O(1) — fixed-size vowel set, two counters.

Example:
    Input:  "Hello World"
    Output: Vowels = 3, Consonants = 7
============================================================
"""

# Vowel set defined as a module-level constant for reuse
VOWELS = frozenset("aeiou")


def count_vowels_consonants(s: str) -> tuple:
    """
    Count the number of vowels and consonants in a string.

    Non-alphabetic characters (spaces, digits, symbols) are ignored.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple (vowels, consonants) with integer counts.
    """
    vowels = 0
    consonants = 0

    for char in s.lower():
        if char.isalpha():
            if char in VOWELS:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


if __name__ == "__main__":
    # Test Case 1: General case with spaces
    s1 = "Hello World"
    v1, c1 = count_vowels_consonants(s1)
    print(f"Input:      '{s1}'")
    print(f"Vowels:     {v1}")    # Expected: 3
    print(f"Consonants: {c1}")    # Expected: 7

    print()

    # Test Case 2: All vowels
    s2 = "aeiou"
    v2, c2 = count_vowels_consonants(s2)
    print(f"Input:      '{s2}'")
    print(f"Vowels:     {v2}")    # Expected: 5
    print(f"Consonants: {c2}")    # Expected: 0

    print()

    # Test Case 3: Mixed with numbers and symbols
    s3 = "Python 3.11!"
    v3, c3 = count_vowels_consonants(s3)
    print(f"Input:      '{s3}'")
    print(f"Vowels:     {v3}")    # Expected: 2
    print(f"Consonants: {c3}")    # Expected: 5

    print()

    # Test Case 4: Uppercase letters
    s4 = "DATA STRUCTURES"
    v4, c4 = count_vowels_consonants(s4)
    print(f"Input:      '{s4}'")
    print(f"Vowels:     {v4}")    # Expected: 5
    print(f"Consonants: {c4}")    # Expected: 10

    print()

    # Test Case 5: Empty string
    s5 = ""
    v5, c5 = count_vowels_consonants(s5)
    print(f"Input:      '{s5}'")
    print(f"Vowels:     {v5}")    # Expected: 0
    print(f"Consonants: {c5}")    # Expected: 0

    print()

    # Test Case 6: Only non-alphabetic characters
    s6 = "12345 !@#"
    v6, c6 = count_vowels_consonants(s6)
    print(f"Input:      '{s6}'")
    print(f"Vowels:     {v6}")    # Expected: 0
    print(f"Consonants: {c6}")    # Expected: 0
