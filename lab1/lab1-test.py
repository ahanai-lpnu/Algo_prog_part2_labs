import unittest
from lab1 import find_longest_peak

class TestLongestPeak(unittest.TestCase):
    def test_example_from_task(self):
        array = [1, 3, 5, 4, 2, 8, 3, 7]
        self.assertEqual(find_longest_peak(array), 5)
        print(find_longest_peak(array))

    def test_sorted_ascending(self):
        array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(find_longest_peak(array), 0)
        print(find_longest_peak(array))

    def test_sorted_descending(self):
        array = [6, 5, 4, 3, 2, 1]
        self.assertEqual(find_longest_peak(array), 0)
        print(find_longest_peak(array))

    def test_two_els(self):
        array = [10, 20]
        self.assertEqual(find_longest_peak(array), 0)
        print(find_longest_peak(array))

    def test_no_peaks(self):
        array = [-1, -5, -1]
        array = [2, 2, 2, 2, 2]
        self.assertEqual(find_longest_peak(array), 0)
        self.assertEqual(find_longest_peak(array), 0)
        print(find_longest_peak(array))
        print(find_longest_peak(array))


    def test_three_peaks(self):
        array = [0, 5, 0, 2, 6, 4, 2, 1, 3, 1]
        self.assertEqual(find_longest_peak(array), 6)
        print(find_longest_peak(array))


if __name__ == '__main__':
    unittest.main(verbosity=2)