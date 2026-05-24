import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from lab9 import Trie, build_trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.patterns = ["apple", "app", "application", "bat", "batch", "cat"]
        self.trie = build_trie(self.patterns)

    def test_insert_and_search_existing_words(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("batch"))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("batman"))
        self.assertFalse(self.trie.search("ca"))

    def test_starts_with_existing_prefix(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("bat"))
        self.assertTrue(self.trie.starts_with("c"))

    def test_starts_with_non_existing_prefix(self):
        self.assertFalse(self.trie.starts_with("dog"))
        self.assertFalse(self.trie.starts_with("cats"))

    def test_empty_string(self):
        empty_trie = build_trie([""])
        self.assertTrue(empty_trie.search(""))
        self.assertTrue(empty_trie.starts_with(""))
        self.assertFalse(empty_trie.search("a"))


if __name__ == "__main__":
    unittest.main()