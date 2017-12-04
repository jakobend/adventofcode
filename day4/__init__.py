"""
Solutions for day 4 of the Advent of Code 2017.
"""

from itertools import combinations, permutations

def is_simple_passphrase(phrase):
    """
    Checks whether a phrase contains no repeated words.
    >>> is_simple_passphrase(["aa", "bb", "cc", "dd", "ee"])
    True
    >>> is_simple_passphrase(["aa", "bb", "cc", "dd", "aa"])
    False
    >>> is_simple_passphrase(["aa", "bb", "cc", "dd", "aaa"])
    True
    """
    return not any(phrase.count(word) > 1 for word in phrase)

def is_anagram_passphrase(phrase):
    """
    Checks whether a phrase contains no words that are anagrams of other words.
    >>> is_anagram_passphrase(["abcde", "fghij"])
    True
    >>> is_anagram_passphrase(["abcde", "xyz", "ecdab"])
    False
    >>> is_anagram_passphrase(["a", "ab", "abc", "abd", "abf", "abj"])
    True
    >>> is_anagram_passphrase(["iiii", "oiii", "ooii", "oooi", "oooo"])
    True
    >>> is_anagram_passphrase(["oiii", "ioii", "iioi", "iiio"])
    False
    """
    return not any(
        any(
            first_word == "".join(permutated_word)
            for permutated_word in permutations(second_word)
        )
        for first_word, second_word in combinations(phrase, 2)
    )
