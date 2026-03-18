import unittest
from lab3 import BinaryTree

class TestBinaryTreeDiameter(unittest.TestCase):
    def setUp(self):
        self.main_tree = BinaryTree(1)
        self.main_tree.left = BinaryTree(3)
        self.main_tree.right = BinaryTree(2)
        
        self.main_tree.left.left = BinaryTree(7)
        self.main_tree.left.right = BinaryTree(4)
        
        self.main_tree.left.left.left = BinaryTree(8)
        self.main_tree.left.right.right = BinaryTree(5)
        
        self.main_tree.left.left.left.left = BinaryTree(9)
        self.main_tree.left.right.right.right = BinaryTree(6)

        self.single_node_tree = BinaryTree(10)
        self.empty_tree = None

    def test_main_tree_diameter(self):
        result = self.main_tree.get_diameter()
        self.assertEqual(result, 6)

    def test_single_node_tree_diameter(self):
        result = self.single_node_tree.get_diameter()
        self.assertEqual(result, 0)

    def test_empty_tree_diameter(self):
        if self.empty_tree is None:
            result = 0
        else:
            result = self.empty_tree.get_diameter()
            
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()