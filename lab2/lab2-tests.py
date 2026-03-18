import unittest
from lab2 import solve_aggressive_cows

class TestAggressiveCows(unittest.TestCase):
    
    def test_example_case(self):
        n = 5
        c = 3
        sections = [1, 2, 8, 4, 9]
        expected = 3
        self.assertEqual(solve_aggressive_cows(n, c, sections), expected)
        
    def test_simple_case(self):
        n = 3
        c = 2
        sections = [1, 5, 10]
        expected = 9 
        self.assertEqual(solve_aggressive_cows(n, c, sections), expected)

    def test_impossible_large_gap(self):
        n = 5
        c = 5
        sections = [1, 2, 3, 4, 5]
        expected = 1
        self.assertEqual(solve_aggressive_cows(n, c, sections), expected)

if __name__ == '__main__':
    unittest.main()