"""
============================================================
Problem: Count the Number of Words in a String
============================================================

Problem Statement:
    Given a string (a sentence or paragraph), count the
    number of words in it. A word is defined as a sequence
    of non-whitespace characters separated by one or more
    spaces (or other whitespace).

    Handle edge cases:
    - Leading/trailing spaces
    - Multiple consecutive spaces between words
    - Empty string

Approach:
    - Use str.split() which splits on any whitespace and
      automatically handles multiple spaces, tabs, and
      leading/trailing whitespace.
    - The length of the resulting list is the word count.

    Manual Approach (also shown):
    - Iterate through the string character by character.
    - Track whether we are "inside" a word using a boolean flag.
    - Increment count each time we transition from whitespace
      to a non-whitespace character.

Time Complexity:  O(n) — single pass through the string.
Space Complexity:
    - Built-in: O(n) — split() creates a list of words.
    - Manual:   O(1) — only a counter and a flag are used.

Example:
    Input:  "  Hello   World  from Python  "
    Output: 4
============================================================
"""


def count_words(s: str) -> int:
    """
    Count the number of words in a string using str.split().

    Handles multiple spaces, tabs, and leading/trailing whitespace.

    Args:
        s (str): The input string.

    Returns:
        int: The number of words in the string.
    """
    # split() with no argument splits on any whitespace and
    # removes empty strings from multiple spaces automatically
    return len(s.split())


def count_words_manual(s: str) -> int:
    """
    Count the number of words using manual character iteration.

    Uses O(1) extra space — no list creation.

    Args:
        s (str): The input string.

    Returns:
        int: The number of words in the string.
    """
    count = 0
    in_word = False

    for char in s:
        if char != ' ' and not in_word:
            # Transition: whitespace → word character
            in_word = True
            count += 1
        elif char == ' ':
            # Transition: word character → whitespace
            in_word = False

    return count


if __name__ == "__main__":
    # Test Case 1: Multiple spaces between words
    s1 = "  Hello   World  from Python  "
    print(f"Input:         '{s1}'")
    print(f"Count (builtin): {count_words(s1)}")        # Expected: 4
    print(f"Count (manual):  {count_words_manual(s1)}") # Expected: 4

    print()

    # Test Case 2: Normal sentence
    s2 = "The quick brown fox"
    print(f"Input:           '{s2}'")
    print(f"Count (builtin): {count_words(s2)}")        # Expected: 4
    print(f"Count (manual):  {count_words_manual(s2)}") # Expected: 4

    print()

    # Test Case 3: Single word
    s3 = "Python"
    print(f"Input:           '{s3}'")
    print(f"Count (builtin): {count_words(s3)}")        # Expected: 1
    print(f"Count (manual):  {count_words_manual(s3)}") # Expected: 1

    print()

    # Test Case 4: Only spaces
    s4 = "     "
    print(f"Input:           '{s4}'")
    print(f"Count (builtin): {count_words(s4)}")        # Expected: 0
    print(f"Count (manual):  {count_words_manual(s4)}") # Expected: 0

    print()

    # Test Case 5: Empty string
    s5 = ""
    print(f"Input:           '{s5}'")
    print(f"Count (builtin): {count_words(s5)}")        # Expected: 0
    print(f"Count (manual):  {count_words_manual(s5)}") # Expected: 0

    print()

    # Test Case 6: Single character word
    s6 = "I am a student"
    print(f"Input:           '{s6}'")
    print(f"Count (builtin): {count_words(s6)}")        # Expected: 4
    print(f"Count (manual):  {count_words_manual(s6)}") # Expected: 4
