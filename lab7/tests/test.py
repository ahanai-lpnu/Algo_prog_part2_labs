import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lab7 import calculate_max_flow

class TestFlow(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("src"):
            os.makedirs("src")
        self.path = os.path.join("src", "roads.csv")

    def test_simple_flow(self):
        with open(self.path, "w") as f:
            f.write("F1\nS1\nF1, X1, 10\nX1, S1, 7")
        self.assertEqual(calculate_max_flow(self.path), 7)

    def test_bottleneck(self):
        with open(self.path, "w") as f:
            f.write("F1, F2\nS1\nF1, X1, 10\nF2, X1, 10\nX1, S1, 12")
        self.assertEqual(calculate_max_flow(self.path), 12)

if __name__ == "__main__":
    unittest.main()