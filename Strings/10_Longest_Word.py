"""
============================================================
Problem: Find the Longest Word in a String
============================================================

Problem Statement:
    Given a string (a sentence), find and return the longest
    word. If there are multiple words with the same maximum
    length, return the first one encountered.
    Punctuation attached to words is stripped before comparison.

Approach:
    - Split the string into words using str.split().
    - Strip common punctuation from each word using str.strip().
    - Track the longest word seen so far using a variable.
    - Update it whenever a longer word is found.
    - Return the longest word after the loop.

    Why strip punctuation?
    - "world!" and "world" should be treated the same length.
    - str.strip(punctuation) removes leading/trailing symbols.

Time Complexity:  O(n) — split is O(n), loop over words is O(n).
Space Complexity: O(n) — list of words created by split().

Example:
    Input:  "I love programming in Python"
    Output: "programming"  (11 characters)
============================================================
"""

import string


def find_longest_word(sentence: str) -> str:
    """
    Find the longest word in a sentence.

    Punctuation attached to words is stripped before comparison.
    Returns the first word in case of a tie.

    Args:
        sentence (str): The input sentence or string of words.

    Returns:
        str: The longest word found, or an empty string if the
             sentence is empty or contains only whitespace.
    """
    words = sentence.split()

    if not words:
        return ""

    longest = ""

    for word in words:
        # Strip punctuation from both ends of each word
        clean_word = word.strip(string.punctuation)

        if len(clean_word) > len(longest):
            longest = clean_word

    return longest


def find_longest_word_with_length(sentence: str) -> tuple:
    """
    Find the longest word and return it along with its length.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: (longest_word, length) or ("", 0) if empty.
    """
    word = find_longest_word(sentence)
    return word, len(word)


if __name__ == "__main__":
    # Test Case 1: General sentence
    s1 = "I love programming in Python"
    word1, length1 = find_longest_word_with_length(s1)
    print(f"Input:        '{s1}'")
    print(f"Longest Word: '{word1}' ({length1} characters)")
    # Expected: 'programming' (11)

    print()

    # Test Case 2: Tie — returns first longest
    s2 = "cat bat dog"
    word2, length2 = find_longest_word_with_length(s2)
    print(f"Input:        '{s2}'")
    print(f"Longest Word: '{word2}' ({length2} characters)")
    # Expected: 'cat' (first occurrence)

    print()

    # Test Case 3: Sentence with punctuation
    s3 = "Hello, world! This is amazing."
    word3, length3 = find_longest_word_with_length(s3)
    print(f"Input:        '{s3}'")
    print(f"Longest Word: '{word3}' ({length3} characters)")
    # Expected: 'amazing' (7)

    print()

    # Test Case 4: Single word
    s4 = "Algorithms"
    word4, length4 = find_longest_word_with_length(s4)
    print(f"Input:        '{s4}'")
    print(f"Longest Word: '{word4}' ({length4} characters)")
    # Expected: 'Algorithms' (10)

    print()

    # Test Case 5: Empty string
    s5 = ""
    word5, length5 = find_longest_word_with_length(s5)
    print(f"Input:        '{s5}'")
    print(f"Longest Word: '{word5}' ({length5} characters)")
    # Expected: '' (0)

    print()

    # Test Case 6: DSA-themed sentence
    s6 = "Data Structures and Algorithms are fundamental to engineering"
    word6, length6 = find_longest_word_with_length(s6)
    print(f"Input:        '{s6}'")
    print(f"Longest Word: '{word6}' ({length6} characters)")
    # Expected: 'fundamental' (11)
