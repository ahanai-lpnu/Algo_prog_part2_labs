import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lab8 import find_longest_chain


class TestWchain(unittest.TestCase):

    def test_example_1(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        expected_result = 6
        self.assertEqual(find_longest_chain(words), expected_result)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        expected_result = 4
        self.assertEqual(find_longest_chain(words), expected_result)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        expected_result = 1
        self.assertEqual(find_longest_chain(words), expected_result)

    def test_empty_list(self):
        self.assertEqual(find_longest_chain([]), 0)

    def test_single_word(self):
        words = ["singleton"]
        self.assertEqual(find_longest_chain(words), 1)

    def test_duplicates_in_list(self):
        words = ["a", "ab", "abc", "ab", "a"]
        expected_result = 3
        self.assertEqual(find_longest_chain(words), expected_result)


if __name__ == "__main__":
    unittest.main()