"""
============================================================
Problem: Find the Frequency of Each Character in a String
============================================================

Problem Statement:
    Given a string, count how many times each character
    appears and return the result as a dictionary.
    The frequency count is case-sensitive by default, with
    an option for case-insensitive counting.

Approach (Hash Map / Dictionary):
    - Use a dictionary to store character → count mappings.
    - Iterate through each character in the string.
    - For each character, increment its count in the dict
      (use dict.get(char, 0) + 1 to handle first occurrences).
    - Return the completed frequency dictionary.

    This is the classic frequency-counting pattern using
    a hash map, which is fundamental to many string problems
    (anagram check, first non-repeating character, etc.).

Time Complexity:  O(n) — single pass through the string.
Space Complexity: O(k) — where k is the number of unique
                         characters (at most O(1) for fixed
                         alphabet, O(n) worst case).

Example:
    Input:  "banana"
    Output: {'b': 1, 'a': 3, 'n': 2}
============================================================
"""


def character_frequency(s: str, case_sensitive: bool = True) -> dict:
    """
    Count the frequency of each character in a string.

    Args:
        s (str): The input string.
        case_sensitive (bool): If False, treats 'A' and 'a' as
                               the same character. Default is True.

    Returns:
        dict: A dictionary mapping each character to its count.
    """
    if not case_sensitive:
        s = s.lower()

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    return freq


def display_frequency(freq: dict) -> None:
    """
    Display character frequencies in a readable sorted format.

    Args:
        freq (dict): A character frequency dictionary.
    """
    for char, count in sorted(freq.items()):
        # Visual bar makes frequency easy to read at a glance
        bar = "#" * count
        print(f"  '{char}': {count:>3}  {bar}")


if __name__ == "__main__":
    # Test Case 1: Classic example
    s1 = "banana"
    freq1 = character_frequency(s1)
    print(f"Input: '{s1}'")
    print("Frequency:")
    display_frequency(freq1)
    # Expected: {'a': 3, 'b': 1, 'n': 2}

    print()

    # Test Case 2: String with spaces
    s2 = "hello world"
    freq2 = character_frequency(s2)
    print(f"Input: '{s2}'")
    print("Frequency:")
    display_frequency(freq2)

    print()

    # Test Case 3: Case-insensitive counting
    s3 = "AaBbCc"
    freq3 = character_frequency(s3, case_sensitive=False)
    print(f"Input: '{s3}' (case-insensitive)")
    print("Frequency:")
    display_frequency(freq3)
    # Expected: {'a': 2, 'b': 2, 'c': 2}

    print()

    # Test Case 4: All same characters
    s4 = "aaaaa"
    freq4 = character_frequency(s4)
    print(f"Input: '{s4}'")
    print("Frequency:")
    display_frequency(freq4)
    # Expected: {'a': 5}

    print()

    # Test Case 5: Empty string
    s5 = ""
    freq5 = character_frequency(s5)
    print(f"Input: '{s5}'")
    print(f"Frequency: {freq5}")
    # Expected: {}
